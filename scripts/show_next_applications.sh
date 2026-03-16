#!/bin/bash
# Show next batch of applications ready to submit

python3 << 'EOF'
import openpyxl

wb = openpyxl.load_workbook('/sessions/gifted-charming-mayer/mnt/me/Job_Opportunities_CLEANED.xlsx')
ws = wb.active

batch_size = 10
batch = []

for idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True), 1):
    company = row[1]
    role = row[2]
    tier = row[7]
    link = row[9]
    fit_score = row[6]

    if tier == "EXCELLENT" and len(batch) < batch_size:
        batch.append({
            'idx': idx,
            'company': company,
            'role': role,
            'fit': fit_score,
            'link': link
        })

print("\n🎯 NEXT 10 APPLICATIONS - EXCELLENT TIER\n")
print("=" * 120)
print(f"{'#':<4} {'Company':<25} {'Role':<40} {'Fit':<4} {'Link':<45}")
print("=" * 120)

for i, app in enumerate(batch, 1):
    link_preview = (app['link'][:43] + "...") if len(str(app['link'])) > 45 else app['link']
    print(f"{i:<4} {str(app['company'])[:23]:<25} {str(app['role'])[:38]:<40} {app['fit']:<4} {str(link_preview):<45}")

print("=" * 120)
print(f"\n✓ Ready to apply: {len(batch)} opportunities\n")

print("QUICK START:")
print("1. Open: /Application_Tracker.xlsx")
print("2. Copy cover letter from: /Cover_Letters/EXCELLENT/{role_number}_{company}.txt")
print("3. Apply on job board using the link above")
print("4. Update tracker with Date Applied and Status: 'Applied'")
print()

EOF
