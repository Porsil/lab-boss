# Table of Contents
- [Validator Testing](#validator-testing)
  * [HTML](#html)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser and Device Testing](#browser-and-device-testing)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)

# Validator Testing

## HTML

The [Official W3C HTML Validator](https://validator.w3.org/) was used to check all html pages. All errors found were fixed.

<details>

<summary>HTML Validation Report</summary>

| Page                     | Logged Out    | Logged In - Analyst | Logged In - Senior |
|--------------------------|:-------------:|:-------------------:|:------------------:|
| login.html               | Note 1        | N/A                 | N/A                |
| logout.html              | N/A           | Note 1              | Note 1             |
| signup.html              | Note 1        | N/A                 | N/A                |
| 400.html                 | Note 2 & 3    | N/A                 | N/A                |
| 403.html                 | N/A           | Note 3              | Note 3             |
| 404.html                 | Note 3        | N/A                 | N/A                |
| 500.html                 | Note 3        | N/A                 | N/A                |
| base.html                | Note 1        | Note 1              | Note 1             |
| index.html               | No errors     | No errors           | No errors          |
| contact_us.html          | No errors     | No errors           | No errors          |
| tracker.html             | N/A           | No errors           | No errors          |
| all_tracker.html         | N/A           | No errors           | No errors          |
| priority_tracker.html    | N/A           | No errors           | No errors          |
| add_batch.html           | N/A           | No errors           | No errors          |
| update_batch.html        | N/A           | N/A                 | No errors          |
| delete_batch.html        | N/A           | N/A                 | No errors          |
| material.html            | N/A           | N/A                 | No errors          |
| add_material.html        | N/A           | N/A                 | No errors          |
| update_material.html     | N/A           | N/A                 | No errors          |
| delete_material.html     | N/A           | N/A                 | No errors          |
| scheduler.html           | N/A           | Note 4              | Note 4             |
| all_scheduler.html       | N/A           | Note 4 & 5          | Note 4 & 5         |
| add_workload.html        | N/A           | No errors           | No errors          |
| update_workload.html     | N/A           | No errors           | No errors          |
| delete_workload.html     | N/A           | N/A                 | No errors          |
| all_delete_workload.html | N/A           | N/A                 | No errors          |
| analysts.html            | N/A           | N/A                 | No errors          |
| add_analyst.html         | N/A           | N/A                 | No errors          |
| update_analyst.html      | N/A           | N/A                 | No errors          |
| delete_analyst.html      | N/A           | N/A                 | No errors          |
| tests.html               | N/A           | N/A                 | No errors          |
| add_test.html            | N/A           | N/A                 | No errors          |
| update_test.html         | N/A           | N/A                 | No errors          |
| delete_test.html         | N/A           | N/A                 | No errors          |

</details>

<details>

<summary>HTML Validation Notes</summary>

### Notes

- Note 1:
login.html, logout.html, signup.html and base.html all had a trailing slash.
The trailing slash was removed to fix the error.

- Note 2:
400.html had an extra `</div>` that was not required.
This was removed to fix the error.

- Note 3:
All 4 error pages had the heading of `<h3>Lab Boss</h1>`.
The closing tag was changed to `</h3>` to fix the error.

- Note 4:
The icon links and toggle card form were enclosed in `<p></p>` tags.
The `<p></p>` tags were changed to `<div></div>` tags to fix the error.

- Note 5:
Page contained `<strike></strike>` tags, which are obsolete.
To fix the error these tags were removed and CSS was added to line through the required text.

</details>

[Table Of Contents](#table-of-contents)

## CSS

The [Official W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check the style.css file. No errors were found.

<details>

<summary>CSS Validation Report</summary>

![CSS Validation](readme_assets/css_validator.png)

</details>

[Table Of Contents](#table-of-contents)

## JavaScript

[Jshint](https://jshint.com/) was used to check all JavaScript code. No errors were found.

<details>

<summary>Jshint Reports</summary>

![Jshint - message timeout](readme_assets/messages_jshint.png)
![Jshint - map](readme_assets/map_jshint.png)
</details>

[Table Of Contents](#table-of-contents)

## Python

The python code was checked using the PEP8 linter throughout the project. The linter detected numerous issues with the code relating to whitespace and lines being too long. These issues were fixed by deleting any whitespaces and changing the long lines to multi-line code. Any code flagged for these issues that was not written by me has not been changed.

[Table Of Contents](#table-of-contents)

## Lighthouse

All pages were run for Lighthouse validation on both desktop and mobile to assess performance and accessibility. Initial reports gave the images should be in webp format and 'aria-labels' were missing for icon buttons. These were fixed by converting the images to webp format and adding aria-labels to the icon buttons.
The Lighthouse report gave give a warning for *'Background and foreground colors do not have a sufficient contrast ratio'*, the contrast was improved on the home page and the tracker table. This issue was ignored for the footer link to the logo attribute as the link is not an integral part of the site but a requirement for use of the logo hexagon.

After the updates given above the following scores were given:

<details>

<summary>Lighthouse Desktop Report</summary>

| Page                | Performance  | Accessibility | Best Practices  | SEO  |
|---------------------|:------------:|:-------------:|:---------------:|:----:|
| login               | 99           | 97            | 100             | 100  |
| logout              | 99           | 98            | 100             | 100  |
| signup              | 99           | 97            | 100             | 100  |
| home                | 99           | 97            | 100             | 100  |
| contact_us          | 99           | 98            | 92 (Note 6)     | 100  |
| tracker             | 99           | 98            | 100             | 100  |
| all_tracker         | 98           | 98            | 100             | 100  |
| priority_tracker    | 99           | 98            | 100             | 100  |
| add_batch           | 98           | 98            | 100             | 100  |
| update_batch        | 98           | 98            | 100             | 100  |
| delete_batch        | 98           | 98            | 100             | 100  |
| material            | 99           | 98            | 100             | 100  |
| add_material        | 98           | 98            | 100             | 100  |
| update_material     | 98           | 98            | 100             | 100  |
| delete_material     | 98           | 98            | 100             | 100  |
| scheduler           | 98           | 98            | 100             | 100  |
| all_scheduler       | 98           | 98            | 100             | 100  |
| add_workload        | 98           | 98            | 100             | 100  |
| update_workload     | 98           | 98            | 100             | 100  |
| delete_workload     | 98           | 98            | 100             | 100  |
| all_delete_workload | 98           | 98            | 100             | 100  |
| analysts            | 99           | 98            | 100             | 100  |
| add_analyst         | 99           | 98            | 100             | 100  |
| update_analyst      | 98           | 98            | 100             | 100  |
| delete_analyst      | 98           | 98            | 100             | 100  |
| tests               | 99           | 98            | 100             | 100  |
| add_test            | 98           | 98            | 100             | 100  |
| update_test         | 98           | 98            | 100             | 100  |
| delete_test         | 98           | 98            | 100             | 100  |

- Note 6:
The Lightouse best practies score was lower for the contact us page due to the map pin. This was ignored as the map was generated using an API.

![Lightouse Map](readme_assets/map_lighthouse.png)

</details>

<details>

<summary>Lighthouse Mobile Report</summary>

Due to the site being desiged for use in a laboratory, it is unlikely to be used on a mobile device. The mobile report was performed as site has been designed to be responsive so the browser size can be shrunk if desired.

The main issue reported for mobile devices was the font size of the logo attribute text and the copyright text in the footer are too small. This issue was not addressed due to these not being an integral part of the sites usage.

| Page                | Performance  | Accessibility | Best Practices  | SEO  |
|---------------------|:------------:|:-------------:|:---------------:|:----:|
| login               | 88           | 97            | 100             | 98   |
| logout              | 88           | 97            | 100             | 92   |
| signup              | 89           | 97            | 100             | 92   |
| home                | 94           | 98            | 100             | 92   |
| contact_us          | 85           | 98            | 92              | 92   |
| tracker             | 91           | 97            | 100             | 95   |
| all_tracker         | 91           | 97            | 100             | 97   |
| priority_tracker    | 94           | 97            | 100             | 95   |
| add_batch           | 88           | 97            | 100             | 92   |
| update_batch        | 88           | 97            | 100             | 92   |
| delete_batch        | 88           | 97            | 100             | 100  |
| material            | 91           | 97            | 100             | 93   |
| add_material        | 88           | 97            | 100             | 92   |
| update_material     | 89           | 97            | 100             | 92   |
| delete_material     | 88           | 97            | 100             | 100  |
| scheduler           | 83           | 97            | 100             | 98   |
| all_scheduler       | 86           | 97            | 100             | 98   |
| add_workload        | 88           | 97            | 100             | 92   |
| update_workload     | 88           | 97            | 100             | 92   |
| delete_workload     | 88           | 97            | 100             | 100  |
| all_delete_workload | 88           | 97            | 100             | 100  |
| analysts            | 86           | 97            | 100             | 100  |
| add_analyst         | 88           | 97            | 100             | 92   |
| update_analyst      | 89           | 97            | 100             | 92   |
| delete_analyst      | 88           | 97            | 100             | 100  |
| tests               | 86           | 97            | 100             | 85   |
| add_test            | 89           | 97            | 100             | 92   |
| update_test         | 88           | 97            | 100             | 92   |
| delete_test         | 88           | 97            | 100             | 100  |

</details>

[Table Of Contents](#table-of-contents)

## Browser and Device Testing

The site was developed and continuously tested on a desktop using Google Chrome, including using the developer tools to check the responsiveness across multiple device sizes. 

The site was checked on a desktop post depolyment using Firefix and Microsoft Edge and on a iPhone 12 using Safari.

No issues were noted.

[Table Of Contents](#table-of-contents)

## Manual Testing

### Site Navigation

| Feature                  | Action     | Expected Result                      | Pass/Fail |
|--------------------------|------------|--------------------------------------|-----------|
| Screen size above 992px  |                                                               |
| Logged Out                                                                               |
| Site logo                | Click      | Open Home page                       | Pass      |
| Login Link               | Click      | Open Login page                      | Pass      |
| Register Link            | Click      | Open Signup page                     | Pass      |
| Nav options available    | Display    | No further nav options are available | Pass      |
| All Nav Links            | Hover      | Change text colour                   | Pass      |
| Logged in as Analyst                                                                     |
| Site logo                | Click      | Open Home page                       | Pass      |
| Batch Tracker Link       | Click      | Open Tracker page                    | Pass      |
| Scheduler Link           | Click      | Open Scheduler page                  | Pass      |
| Logout Link              | Click      | Open Logout page                     | Pass      |
| Nav options available    | Display    | No further nav options are available | Pass      |
| All Nav Links            | Hover      | Change text colour                   | Pass      |
| Logged in as Senior Analyst                                                              |
| Site logo                | Click      | Open Home page                       | Pass      |
| Batch Tracker Link       | Click      | Open Tracker page                    | Pass      |
| Scheduler Link           | Click      | Open Scheduler page                  | Pass      |
| Data Management Dropdown | Click      | Displays dropdown options            | Pass      |
| Materials Link           | Click      | Open Tracker page                    | Pass      |
| Analysts Link            | Click      | Open Tracker page                    | Pass      |
| Tests Link               | Click      | Open Tracker page                    | Pass      |
| Admin Link               | Click      | Open Tracker page                    | Pass      |
| Logout Link              | Click      | Open Logout page                     | Pass      |
| All Nav Links            | Hover      | Change text colour                   | Pass      |
| Screen size changed from above 992px to below 991px                                      |
| Hamburger menu           | Display    | Navbar changes to hamburger menu     | Pass      |
| Logged Out                                                                               |
| Site logo                | Click      | Open Home page                       | Pass      |
| Login Link               | Click      | Open Login page                      | Pass      |
| Register Link            | Click      | Open Signup page                     | Pass      |
| Nav options available    | Display    | No further nav options are available | Pass      |
| All Nav Links            | Hover      | Change text colour                   | Pass      |
| Logged in as Analyst                                                                     |
| Site logo                | Click      | Open Home page                       | Pass      |
| Batch Tracker Link       | Click      | Open Tracker page                    | Pass      |
| Scheduler Link           | Click      | Open Scheduler page                  | Pass      |
| Logout Link              | Click      | Open Logout page                     | Pass      |
| Nav options available    | Display    | No further nav options are available | Pass      |
| All Nav Links            | Hover      | Change text colour                   | Pass      |
| Logged in as Senior Analyst                                                              |
| Site logo                | Click      | Open Home page                       | Pass      |
| Batch Tracker Link       | Click      | Open Tracker page                    | Pass      |
| Scheduler Link           | Click      | Open Scheduler page                  | Pass      |
| Data Management Dropdown | Click      | Displays dropdown options            | Pass      |
| Materials Link           | Click      | Open Tracker page                    | Pass      |
| Analysts Link            | Click      | Open Tracker page                    | Pass      |
| Tests Link               | Click      | Open Tracker page                    | Pass      |
| Admin Link               | Click      | Open Tracker page                    | Pass      |
| Logout Link              | Click      | Open Logout page                     | Pass      |
| All Nav Links            | Hover      | Change text colour                   | Pass      |



[Table Of Contents](#table-of-contents)

## Bugs


[Table Of Contents](#table-of-contents)
