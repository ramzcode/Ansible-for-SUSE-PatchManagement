# SUSE RMT based repo Sync client activation
## How it works
1. Setup RMT
2. Activate RMT using the Mirror Credentials from the SCC portal.
3. copy the rmt-client-setup from the RMT server to the clients - /usr/share/rmt/public/tools/
4. SUSEConnect -d
5. SUSEConnect --cleanup
6. ./rmt-client-setup --host rmtserver.ramzcode.com  ## Answer Y to question or pass CLI parameter to use within a script
7. SUSEConnect -s
8. zypper ref

