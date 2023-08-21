# SUSE RMT based repo Sync client activation
## How it works
1. Setup RMT
    - sudo zypper in rmt-server or zypper install rmt-server yast2-rmt nginx mariadb
    - systemctl enable --now mariadb
    - sudo yast2 rmt
    - chown -R _rmt:nginx /usr/share/rmt/config
2. Activate RMT using the Mirror Credentials from the SCC portal and the add product / Sync / mirror
    - rmt-cli sync
    - rmt-cli mirror
3. copy the rmt-client-setup from the RMT server to the clients - /usr/share/rmt/public/tools/
4. SUSEConnect -d
5. SUSEConnect --cleanup
6. ./rmt-client-setup --host rmtserver.ramzcode.com  ## Answer Y to question or pass CLI parameter to use within a script
7. SUSEConnect -s
8. zypper ref
> [!NOTE]
> * Make sure only needed products and Architecture is selected
> * To use a different Filesystem or mount point as the repo data path please use - ln -sfn TARGET /usr/share/rmt/public/repo

> [!WARNING]
> If the repo dir storage is not planned well, you may end up with full utlilized disk and a data loss which we are not responsible.
