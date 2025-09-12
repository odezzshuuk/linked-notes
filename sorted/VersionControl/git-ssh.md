# Git - SSH

## Generate SSH Public key

1. Open Git Bash
2. Enter `ssh-keygen -t ed25519 -C "anonymous@example.com"`

> in step 2, use your email address as a label to generate SSH key

- base on ed25519 [algorithm](), generate public/private key pair
- `-t`: specify key type(algorithm type)
- `-C`: provide a comment

3. system prompt `Enter a file in which to save the key(/c/Users/you/.ssh/id_algorithm): [Press Enter]`

- set where to store the key file, enter to accept default

4. prompt to enter passphrase

---

modified passphrase

`ssh-keygen -p -f ~/.ssh/id_ed25519`

file list create in `~/.ssh` by above steps

- id_ed25519
- id_ed25519.pub

## Check Exist SSH keys

1. Open Git Bash
2. Enter `ls -al ~/.ssh`
3. if `public SSH key` already exist, file name may be:
    - id_rsa.pub
    - id_ecdsa.pub
    - id_ed25519.pub

## ssh-agent

- A program used to hold private keys for public key authentication
- Usually started at the beginning of an X-session or login session
- All other programs or windows are started as clients of the ssh-agent

## Algorithm

- RSA
- ECDSA
- Ed25519

