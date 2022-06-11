## How to update

The process of auto update follows the following workflow
1. pull repo from AUR
2. Patch hashs and versions for `linux64`
3. Patch hashs and versions for `linux32`
4. Builds the package
5. If succeeds, generate the commit `[AUTO] Version <version>`
6. Clean up the build folder

Run the following command to update
```sh
$ sh auto_update.sh
```

Dry run (download and build)
```sh
$ SKIP_PUSH=true sh auto_update.sh
```

### Maintainers
Active Maintainers:
- Anderson Rocha <anderson2320@gmail.com>

Previous Maintainers:
- etriguba <eugenetriguba@gmail.com>
- NexAdn <nexadn@yandex.com>
