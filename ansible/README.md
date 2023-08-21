# SUSE RMT based repo Sync client activation
## How it works
1. Setup RMT
         sudo zypper in rmt-server or zypper install rmt-server yast2-rmt nginx mariadb
        systemctl enable --now mariadb
c. sudo yast2 rmt
d. chown -R _rmt:nginx /usr/share/rmt/config
2. Activate RMT using the Mirror Credentials from the SCC portal and the add product / Sync / mirror
a. rmt-cli sync
b. rmt-cli mirror
3. copy the rmt-client-setup from the RMT server to the clients - /usr/share/rmt/public/tools/
4. SUSEConnect -d
5. SUSEConnect --cleanup
6. ./rmt-client-setup --host rmtserver.ramzcode.com  ## Answer Y to question or pass CLI parameter to use within a script
7. SUSEConnect -s
8. zypper ref

