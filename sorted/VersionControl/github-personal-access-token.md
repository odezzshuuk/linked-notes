# Git - Personal Access Token

## Create

- Settings -> Developer settings -> Personal access tokens
- Set name
- Set Expiration
- Set permissions
- Click Generate token

## Usage

- when access remote repository via https, provide token instead of password

```bash
$ git clone https://github.com/username/repo.git
Username: your_username
Password: your_token
```
