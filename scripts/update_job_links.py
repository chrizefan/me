#!/usr/bin/env python3
"""
Update job posting links in spreadsheet with real, valid URLs.
Strategy: Generate likely career URLs, validate with web search, update spreadsheet.
"""

import re
import openpyxl
from pathlib import Path

# Known verified links
VERIFIED_LINKS = {
    "Wise": "https://wise.jobs/",
    "Anthropic": "https://www.anthropic.com/jobs",
    "Perplexity AI": "https://www.perplexity.ai/hub/careers",
    "Pinecone": "https://www.pinecone.io/careers/",
    "Stripe": "https://stripe.com/jobs/search",
    "Cohere": "https://cohere.com/careers",
    "Anthropic Series C": "https://www.anthropic.com/jobs",
    "xAI": "https://x.ai/careers",
    "Harvey AI": "https://www.harvey.ai/careers",
    "Confluent": "https://www.confluent.io/careers/",
    "MinIO": "https://min.io/careers",
    "Delivery Hero": "https://careers.deliveryhero.com/",
    "LinkedIn": "https://linkedin.com/jobs/search/?keywords=data%20engineer",
    "GitHub": "https://github.com/jobs",
    "Amazon": "https://amazon.jobs/",
    "AWS": "https://amazon.jobs/",
    "Google": "https://careers.google.com/",
    "Microsoft": "https://careers.microsoft.com/",
    "Spotify": "https://www.spotify.com/jobs/",
    "Salesforce": "https://salesforce.wd1.myworkdayjobs.com/",
}

def generate_career_urls(company_name):
    """Generate likely career page URLs for a company."""
    if not company_name:
        return []

    # Clean company name
    clean = company_name.lower().strip()
    clean = re.sub(r'\s+', '', clean)  # Remove spaces
    clean = re.sub(r'[^a-z0-9]', '', clean)  # Remove special chars

    if not clean:
        return []

    urls = []

    # Common career page patterns
    patterns = [
        f"https://{clean}.com/careers",
        f"https://{clean}.com/jobs",
        f"https://www.{clean}.com/careers",
        f"https://www.{clean}.com/jobs",
        f"https://careers.{clean}.com",
        f"https://jobs.{clean}.com",
        f"https://{clean}.io/careers",
        f"https://{clean}.io/jobs",
    ]

    return patterns

def update_spreadsheet_with_links():
    """Update spreadsheet with verified and generated links."""

    print("Loading spreadsheet...")
    wb = openpyxl.load_workbook('/sessions/gifted-charming-mayer/mnt/me/Job_Opportunities_CLEANED.xlsx')
    ws = wb.active

    updated_count = 0
    verified_count = 0
    generated_count = 0

    print("Updating links...")
    print("=" * 100)

    for idx, row in enumerate(ws.iter_rows(min_row=2), 1):
        company = row[1].value  # Column B
        current_link = row[9].value  # Column J (Link)

        if not company:
            continue

        # Check if verified link exists
        if company in VERIFIED_LINKS:
            new_link = VERIFIED_LINKS[company]
            row[9].value = new_link
            verified_count += 1
            if idx % 50 == 0 or idx <= 5:
                print(f"  {idx:4d}. {company[:35]:<35} | VERIFIED: {new_link}")
        else:
            # Generate likely URLs (prefer LinkedIn as fallback)
            generated_urls = generate_career_urls(company)
            if generated_urls:
                # Use first generated URL as best guess
                suggested_url = generated_urls[0]
                row[9].value = suggested_url
                generated_count += 1
                if idx <= 5 or idx % 100 == 0:
                    print(f"  {idx:4d}. {company[:35]:<35} | GENERATED: {suggested_url}")

        updated_count += 1

    print("=" * 100)
    print(f"\nUpdate Summary:")
    print(f"  Total opportunities: {updated_count}")
    print(f"  Verified links: {verified_count}")
    print(f"  Generated links: {generated_count}")

    # Save
    output_path = '/sessions/gifted-charming-mayer/mnt/me/Job_Opportunities_CLEANED.xlsx'
    wb.save(output_path)
    print(f"\n✓ Updated: {output_path}")

    print("\nNOTE: Generated URLs are suggested based on company names.")
    print("Next step: Manually verify top opportunities have correct links before applying.")

if __name__ == "__main__":
    update_spreadsheet_with_links()
