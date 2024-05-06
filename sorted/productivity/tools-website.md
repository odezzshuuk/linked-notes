# Website tools

## quickref

[quickref](https://quickref.me)

## cheat.sh

[cheat.sh](https://github.com/chubin/cheat.sh)

- linux command line tools
- can be use on vim, emacs, vscode, idea.

Install for specific users

```bash
PATH_DIR=$HOME/bin
mkdir -p "$PATH_DIR"
curl https://cht.sh/:cht.sh > "$PATH_DIR/cht.sh"
chmod +x "$PATH_DIR/cht.sh"
```

Install for all users

```bash
curl -s https://cht.sh/:cht.sh | sudo tee /usr/local/bin/cht.sh && sudo chmod +x /usr/local/bin/cht.sh
```

