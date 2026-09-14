# Matching revisions and installed behavior

The three `rewrite/design-first` branches contain new runtime, explanation and UI source. A release identifies an exact commit in each repository. Generated HTTP documentation, the machine contract and UI TypeScript declarations come from the Rust runtime contract. Regeneration must leave the committed contract unchanged.

The runtime packaging script builds the Rust executables with their source revision, builds the UI against that contract, and packages the explanation, technical reference and integration content together. `release.json` identifies the three revisions and SHA-256 digests of packaged files. The installed runtime reports its compiled revision and node release manifest through `/api/release`. The UI distribution carries the matching revision record.

Installation is an ordinary directory containing binaries, UI assets and documents. `./start /path/to/new-node [listen-address]` starts the application with that distribution. It introduces no container or sandbox dependency. The data directory is separate from application files and can be placed wherever the host account has access.

Release validation must check the installed binary, served UI, generated contract and documentation against the manifest. It must also inspect fresh live task evidence. A source build, a browser screenshot or a model's declaration alone does not establish all requested capabilities. The acceptance checklist retains failed and incomplete items until the matching new evidence supports them.

Trusted peer identities and their last explicitly supplied addresses persist across restart. Later messages and transfers can reconnect after an idle connection closes. If a remote node changes its listening endpoint, supply its new peer address; the application does not claim automatic Internet discovery.
