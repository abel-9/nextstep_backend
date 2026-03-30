# Profile Feature Frontend UI Guide

This guide explains how to design and build the Profile user interface in a practical, user-friendly way.

The goal is simple: let a signed-in user view their profile, then add work experience and education entries with clear and easy forms.

## 1) What the user should be able to do

The user should be able to:

- Open their Profile page and see all saved information.
- See two sections: Work Experience and Education.
- Add a new work experience entry.
- Add a new education entry.
- Understand when data is loading, saved, or failed to save.

## 2) Suggested page structure

Use one main page called Profile with this layout:

1. Page header
2. Profile summary card
3. Work Experience section
4. Education section

### A. Page header

- Title: My Profile
- Subtitle: Keep your experience and education up to date.

### B. Profile summary card

Show a simple card at the top with:

- Profile ID (optional to show in UI; useful for support screens)
- User ID (optional to show in UI; usually hidden for regular users)
- Count of work experiences
- Count of education entries

For normal user-facing screens, you can hide IDs and only show counts.

### C. Work Experience section

Include:

- Section title: Work Experience
- Primary action button: Add Work Experience
- List of cards for each entry

Each work experience card should show:

- Position (main text)
- Company (secondary text)
- Start date - End date
- Description (if provided)

### D. Education section

Include:

- Section title: Education
- Primary action button: Add Education
- List of cards for each entry

Each education card should show:

- Major (main text)
- Start date - End date
- Description (if provided)

## 3) Empty states (important)

When there is no data, avoid blank pages.

### Work Experience empty state

- Message: No work experience yet.
- Supporting text: Add your first role to help others understand your background.
- Button: Add Work Experience

### Education empty state

- Message: No education added yet.
- Supporting text: Add your education history so your profile feels complete.
- Button: Add Education

## 4) Form design and field behavior

Use a drawer, modal, or separate page for each add action. Keep forms short and clean.

### A. Add Work Experience form

Fields:

- Company (required, single line text)
- Position (required, single line text)
- Description (optional, multi-line text)
- Start Date (required, date picker)
- End Date (required for now, date picker)

Buttons:

- Primary: Save
- Secondary: Cancel

Inline validation messages:

- Company is required.
- Position is required.
- Start date is required.
- End date is required.
- End date should be after start date.

### B. Add Education form

Fields:

- Major (required, single line text)
- Description (optional, multi-line text)
- Start Date (required, date picker)
- End Date (required for now, date picker)

Buttons:

- Primary: Save
- Secondary: Cancel

Inline validation messages:

- Major is required.
- Start date is required.
- End date is required.
- End date should be after start date.

## 5) Interaction flow to implement

### On page open

1. Show skeleton loading UI for profile sections.
2. Fetch profile data.
3. Replace skeletons with actual content.
4. If no profile data is available yet, show a friendly fallback message and retry action.

### On add entry (work experience or education)

1. User clicks Add button.
2. Form opens.
3. User fills form and clicks Save.
4. Disable Save button and show saving state (Saving...).
5. On success:
- Close form.
- Show toast: Saved successfully.
- Refresh profile data and show new entry.
6. On failure:
- Keep form open.
- Show clear error banner: Could not save. Please try again.

## 6) UX writing (plain, helpful language)

Use short and friendly labels. Example copy:

- Add Work Experience
- Add Education
- Save
- Cancel
- Saving...
- Saved successfully
- Could not load profile. Try again.
- Could not save. Please try again.

Avoid technical words in user-facing text.

## 7) Visual design suggestions

Use a clean, card-based style:

- Soft section separation with spacing.
- Strong section headers.
- Consistent card padding.
- Date text in muted color.
- Primary action button style should be the same across both sections.

Recommended rhythm:

- 24px top-level section spacing.
- 16px card padding.
- 12px spacing between label and input in forms.

## 8) Mobile behavior

For mobile screens:

- Stack all content in one column.
- Keep Add buttons visible near section titles.
- Use full-width buttons in forms.
- Prefer bottom sheet or full-screen form over tiny modal.
- Keep date pickers easy to tap.

## 9) Accessibility checklist

Make sure to include:

- Proper labels for every input.
- Visible focus states for keyboard users.
- Error text connected to the related input.
- Color contrast that is readable.
- Buttons and touch targets that are large enough.

## 10) What to postpone for now

Based on the current profile capability, focus this first frontend version on:

- Viewing profile
- Adding work experience
- Adding education

You can postpone these until later:

- Editing existing entries
- Deleting specific entries
- Reordering entries

## 11) Frontend QA checklist

Before release, verify:

1. Profile loads correctly for signed-in users.
2. Empty states show correctly when no entries exist.
3. Work experience form validates required fields.
4. Education form validates required fields.
5. Save button shows loading state while submitting.
6. Success toast appears and list refreshes after save.
7. Error message appears when request fails.
8. Layout works on both desktop and mobile.

---

If you want, the next step is turning this guide into a complete frontend task breakdown (component list + page wireframe + implementation order).