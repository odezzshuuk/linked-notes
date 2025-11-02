# Web Development - CSRF vs XSS

[CSRF](web-csrf.md)

[XSS](web-xss.md)

## Who Attacks Whom

- Attacker’s target	
  - X: The user of the vulnerable website	
  - C: The vulnerable website itself (via a victim user)
- Attack vector	
  - X: Attacker injects malicious JavaScript into a trusted web application, which is then executed in the browser of any user who views the infected page.	
  - C: Attacker tricks an authenticated user into making an unwanted request to a trusted site (e.g., by clicking a malicious link or loading a hidden form).
- Victim perspective	
  - X: The user’s browser executes malicious script → user’s data or session may be stolen.	
  - C: The web application receives a forged request appearing to come from a legitimate user.
- Primary damage	
  - X: User data theft, credential/session hijacking, malicious actions in user’s context.	
  - C: Unintended actions performed on the web app with the victim’s credentials (e.g., transfer money, change password).

In summary, 

- 👉 XSS attacks users through the website.
- 👉 XSS attacks exploit the trust a user has in a website, 
- 👉 CSRF attacks the website through the user.
- 👉 CSRF attacks exploit the trust a website has in a user.

## Who is Responsible for Prevention

- Website developer	
  - X: ✅ Primary responsibility. Must sanitize inputs, encode outputs, and avoid unsafe APIs.	
  - C: ✅ Primary responsibility. Must implement CSRF tokens and proper cookie configurations.
- Browser	
  - X: 🟨 Helps (via CSP, sandboxing, and escaping mechanisms) but can’t fully prevent it.	
  - C: 🟨 Helps with SameSite cookies and enforcing cross-origin restrictions.
- User	
  - X: 🟥 Little control (can only avoid suspicious sites, disable JS, or use security plugins).	
  - C: 🟨 Some control (avoid clicking suspicious links, log out of sensitive sites).
