
# === Starter Data (OK to run) ===
CLUB_CODE = "AI"

member_ids = [("AI", 1), ("AI", 2), ("AI", 3)]

members = {
    ("AI", 1): {"name": "Ava",   "year": 2, "skills": {"python", "ml"},   "dues_paid": True},
    ("AI", 2): {"name": "Ben",   "year": 1, "skills": {"python"},         "dues_paid": False},
    ("AI", 3): {"name": "Chad",  "year": 3, "skills": {"security", "ml"}, "dues_paid": True},
}

DUES = 25.0

banner = f'Welcome to AI Club - {len(members)} members'
print(banner)

total_expected = DUES * len([member for member in members.values() if not member['dues_paid']])
print(total_expected)

def summarize_member(member):
    return f'''{member['name']} (Year {member['year']}): skills = {', '.join(sorted(member['skills'])) or '<none>'}'''

ava = members[member_ids[0]]
summary_ava = summarize_member(ava)
print(summary_ava)

assert isinstance(banner, str) and "AI Club" in banner
assert isinstance(total_expected, (int, float))
assert isinstance(summary_ava, str) and "Ava" in summary_ava
print("Task 1 basic checks passed.")

def next_id():
    """Return a new tuple like ("AI", next_number)."""
    i = 1
    while (new_id := ('AI', i)) in member_ids:
        i += 1
    return new_id

nid = next_id()
member_ids.append(nid)
members[nid] = {"name": "Dana", "year": 1, "skills": set(), "dues_paid": False}
print("Added:", nid, members[nid])

print('Members:')
for mid,member in members.items():
    print(f'ID {mid}: {summarize_member(member)}')