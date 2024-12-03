# Installation
Download the [roblox model](https://github.com/ernisto/package/releases/download/v1.0.7/model.rbxm), or get the [model](https://create.roblox.com/store/asset/77872017928574/package&assetType=Model).
require by id
```lua
local package = require(77872017928574)
```
or by wally
```toml
package = "ernisto/package@1.0.7"
```

# Development Setup
## Clone Repository
When you install [Git](https://git-scm.com/downloads) if already have not,
run clone this repository with
```sh
git clone https://github.com/ernisto/package
```

learn more: [git cloning an existing repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

## Install Dependencies
Assuming that you already have [Aftman](https://github.com/LPGhatguy/aftman) and [NodeJS](https://nodejs.org) installed into your current user,
install all CLI tools, and run our script to install all wally packages with
```sh
./scripts/init
```

learn more: [wally](https://github.com/UpliftGames/wally?tab=readme-ov-file#wally-install---locked)

## Configure Github Environment
So you planning implement a CI/CD workflow, where you will automatically publish
your place when you push some change, you should configure a environment to be
used by github action
- Publish your repository to [Github](https://github.com)
- Go to `Settings` > `Secrets and variables` > `Actions`
- Create the variable:
    - `HUSKY = 0` to disable client git hooks on github server
    - `CI = true` to disable client hooks on github actions
    - `ASSET_ID` to set your package asset id
    - `TEST_RUNNER_PLACE_ID` to set a place for unit tests be executed
    - `TEST_RUNNER_UNIVERSE_ID` to set a experience for unit tests be executed
- Create the secrets:
    - `ROBLOSECURITY` for your personal roblox cookie [Getting your ROBLOXSECURITY cookie](#getting-your-robloxsecurity-cookie-link)
    - `MANTLE_OPEN_CLOUD_API_KEY` and `TEST_RUNNER_OPEN_CLOUD_API_KEY` for your
    Open Cloud API Key [Creating a Open Cloud API Key](#creating-a-open-cloud-api-key-link)
    - if you are using Amazon AWS or Cloudflare to store your `mantle-state.yml`,
    create `MANTLE_AWS_ACCESS_KEY_ID` and `MANTLE_AWS_SECRET_ACCESS_KEY`

learn more: [using github secrets](https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)

# Useful infos

## Creating a Open Cloud API Key [🔗](#creating-a-open-cloud-api-key-link)
To mantle be able to publish ur place in your account/group,
you should to create a Open Cloud API Key to be used by mantle

- Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
- Click the `Creator Hub` dropdown to select a group if you are creating the API key for a group.
- In the left navigation menu, select `Open Cloud` > `API Keys`.
- Click the `Create API Key` button.
- Enter a unique name for your API key. Such as `MANTLE PUBLISHING API`.
- In the `Access Permissions` section, select an `API System` from the `Select API System`
menu and click the `Add API System` button
- Select the experience that you want to access with the API key.
- From the `Experience Operations` dropdown, select the the operation.

Mantle will requires the following `Operations` from the determinated `API Systems`
- assets
    - asset:read
    - asset:write
- universe-places
    - universe-places:write
- universe
    - universe:write
    - universe.place:write
- notifications
    - user.user-notifications:write

learn more: [roblox open cloud api](https://create.roblox.com/docs/cloud/open-cloud/api-keys) and [mantle authentication](https://mantledeploy.vercel.app/docs/authentication#roblox-open-cloud-api-key)

## Getting your ROBLOXSECURITY cookie [🔗](#getting-your-robloxsecurity-cookie-link)
- Navigate to [roblox](https://roblox.com/) in your browser and open the
`dev tools` (right-click and select `Inspect`).
- Navigate to the `Application` tab, then look for `Cookies` under `Storage` in
the left-hand sidebar.
- Under `Cookies`, select `https://www.roblox.com` then select `.ROBLOSECURITY`
from the list of cookies.
- Copy the value from the `Cookie Value` section.

If there is a logged-in `Roblox Studio` installation, Mantle can automatically
extract its `.ROBLOSECURITY`
cookie and will authenticate requests as the user logged in to Roblox Studio.

learn more: [mantle roblox security](https://mantledeploy.vercel.app/docs/authentication#roblosecurity)