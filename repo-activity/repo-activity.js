/**
 * Compact repo activity — snapshot in the HTML, optional public GitHub refresh.
 * All requests must succeed and validate; the page then swaps every figure at
 * once. Any timeout / non-2xx / malformed payload keeps the snapshot.
 * Stars, forks and watchers are never fetched.
 */
(function () {
  var root = document.getElementById("repo-activity");
  if (!root) return;

  var TIMEOUT_MS = 8000;
  var OWNER = "digithings-ai";
  var REPO = "digithings";
  var BRANCH = "main";
  var WINDOW_DAYS = 30;
  var API = "https://api.github.com";

  function grouped(n) {
    return Number(n).toLocaleString("en-US");
  }

  function isoDay(s) {
    return s ? String(s).slice(0, 10) : "";
  }

  function toIsoZ(d) {
    return d.toISOString().replace(/\.\d{3}Z$/, "Z");
  }

  function isAbort(err) {
    return (
      (err && err.name === "AbortError") ||
      (err instanceof Error && /aborted/i.test(err.message))
    );
  }

  function lastPage(link) {
    if (!link) return null;
    var parts = link.split(",");
    for (var i = 0; i < parts.length; i++) {
      if (parts[i].indexOf('rel="last"') === -1) continue;
      var m = /[?&]page=(\d+)/.exec(parts[i]);
      if (m) return Number(m[1]);
    }
    return null;
  }

  function intCount(v, min) {
    var floor = min == null ? 0 : min;
    if (typeof v !== "number" || !isFinite(v) || Math.floor(v) !== v || v < floor) {
      throw new Error("malformed");
    }
    return v;
  }

  function str(v) {
    if (typeof v !== "string" || !v.trim()) throw new Error("malformed");
    return v;
  }

  function githubUrl(v) {
    var url = str(v);
    if (url.indexOf("https://github.com/") !== 0) throw new Error("malformed");
    return url;
  }

  function fetchJson(url, signal) {
    return fetch(url, { signal: signal }).then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json().then(function (body) {
        return { body: body, headers: res.headers };
      }, function () {
        throw new Error("malformed");
      });
    });
  }

  function commitCount(res) {
    var last = lastPage(res.headers.get("Link") || res.headers.get("link"));
    if (last != null) return last;
    if (!Array.isArray(res.body)) throw new Error("malformed");
    return res.body.length;
  }

  function searchTotal(body) {
    if (!body || typeof body !== "object" || Array.isArray(body)) {
      throw new Error("malformed");
    }
    return intCount(body.total_count);
  }

  function parsePulls(body) {
    if (!body || typeof body !== "object" || Array.isArray(body)) {
      throw new Error("malformed");
    }
    var items = body.items;
    if (items == null) return [];
    if (!Array.isArray(items)) throw new Error("malformed");
    var rows = [];
    for (var i = 0; i < items.length && rows.length < 3; i++) {
      var item = items[i];
      if (!item || typeof item !== "object") continue;
      rows.push({
        number: intCount(item.number, 1),
        title: str(item.title),
        url: githubUrl(item.html_url),
        when: isoDay(item.closed_at || item.updated_at)
      });
    }
    return rows;
  }

  function parseRelease(body) {
    if (!Array.isArray(body)) throw new Error("malformed");
    var first = body[0];
    if (!first || typeof first !== "object") return null;
    return {
      tag: str(first.tag_name),
      url: githubUrl(first.html_url)
    };
  }

  function fill(el, key, value) {
    var nodes = el.querySelectorAll('[data-stat="' + key + '"]');
    for (var i = 0; i < nodes.length; i++) nodes[i].textContent = value;
  }

  function pullRow(item) {
    var li = document.createElement("li");
    li.className = "ra-row";
    var a = document.createElement("a");
    a.className = "ra-num";
    a.href = item.url;
    a.target = "_blank";
    a.rel = "noreferrer";
    a.textContent = "#" + item.number;
    var title = document.createElement("span");
    title.className = "ra-title";
    title.textContent = item.title;
    var date = document.createElement("span");
    date.className = "ra-date";
    date.textContent = item.when;
    li.appendChild(a);
    li.appendChild(title);
    li.appendChild(date);
    return li;
  }

  function apply(live) {
    var rows = live.pulls.map(pullRow);
    fill(root, "commits", grouped(live.commits));
    fill(root, "prs", grouped(live.pullsMerged));
    fill(root, "issues", grouped(live.issuesClosed));
    var rel = root.querySelector('[data-stat="release"]');
    var relLink = root.querySelector('[data-stat="release-url"]');
    if (live.release) {
      if (rel) rel.textContent = live.release.tag;
      if (relLink) relLink.setAttribute("href", live.release.url);
    }
    var list = root.querySelector('[data-stat="recent"]');
    if (list) {
      list.textContent = "";
      rows.forEach(function (li) { list.appendChild(li); });
    }
    fill(root, "freshness", "live " + isoDay(live.generatedAt));
    root.setAttribute("data-source", "live");
  }

  var generatedAt = toIsoZ(new Date());
  var since = new Date(Date.parse(generatedAt) - WINDOW_DAYS * 86400000);
  var sinceIso = toIsoZ(since);
  var sinceDay = sinceIso.slice(0, 10);
  var slug = OWNER + "/" + REPO;
  var controller = new AbortController();
  var timer = setTimeout(function () { controller.abort(); }, TIMEOUT_MS);
  var signal = controller.signal;

  Promise.all([
    fetchJson(
      API + "/repos/" + slug + "/commits?sha=" + encodeURIComponent(BRANCH) +
        "&since=" + sinceIso + "&per_page=1",
      signal
    ),
    fetchJson(
      API + "/search/issues?q=repo:" + slug + "+is:pr+is:merged+merged:>=" +
        sinceDay + "&per_page=3&sort=updated",
      signal
    ),
    fetchJson(
      API + "/search/issues?q=repo:" + slug + "+is:issue+is:closed+closed:>=" +
        sinceDay + "&per_page=1",
      signal
    ),
    fetchJson(API + "/repos/" + slug + "/releases?per_page=1", signal)
  ]).then(function (results) {
    var live = {
      generatedAt: generatedAt,
      commits: commitCount(results[0]),
      pullsMerged: searchTotal(results[1].body),
      issuesClosed: searchTotal(results[2].body),
      release: parseRelease(results[3].body),
      pulls: parsePulls(results[1].body)
    };
    apply(live);
  }).catch(function () {
    /* keep snapshot */
  }).finally(function () {
    clearTimeout(timer);
  });
})();
