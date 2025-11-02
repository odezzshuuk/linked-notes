# Java - Spring Security - ProviderManager

- The most commonly used implementation of [AuthenticationManager](springsecurity-authenticationmanager-interface.md)
- ProviderManager delegates authentication to **multiple** `AuthenticationProvider`s
  - Each `AuthenticationProvider` can indicate the result: success or failure
  - Authentication can indicate that the authentication type is not supported, allowing downstream Providers to continue authentication. If no `Provider` supports it, a `ProviderNotFoundException` is thrown
- By implementing multiple `AuthenticationProvider`s, various authentication methods can be supported, while exposing only a single `AuthenticationManager` instance
- ProviderManager will clear sensitive information (such as passwords) from returned objects

## AuthenticationProvider

- Performs the actual authentication
- Multiple `AuthenticationProvider`s can be injected into the `ProviderManager`
- Each `AuthenticationProvider` has a specific authentication type, for example:
  - DaoAuthenticationProvider: **username/password authentication**
  - JwtAuthenticationProvider: **JWT authentication**

### DaoAuthenticationProvider

1. The filter passes the Authentication to the AuthenticationManager
2. ProviderManager selects DaoAuthenticationProvider
3. DaoAuthenticationProvider calls [UserDetailsService].loadUserByUsername() to obtain a UserDetails object
4. DaoAuthenticationProvider uses [PasswordEncoder] to verify the password
5. If authentication succeeds, an Authentication object is returned, and a UsernamePasswordAuthenticationToken instance is set in the SecurityContextHolder
