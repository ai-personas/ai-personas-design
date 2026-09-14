# Provider integration

Providers expose capability discovery and a decision call. A model request carries the continuing persona, work and environment, selected learning/records/messages/tools, active and selected action results, unread inputs, selected image observations, context size and advertised model facts. Original material is retrieved through paged discovery or persona-authored programs. The runtime does not rank models or impose a compaction schedule.

The Rust `Command` enum is the operation source of truth. It generates server argument validation, structured provider output, UI types and API documentation. The Codex adapter converts this schema to closed structured-output objects, represents optional fields as nullable, and encodes arbitrary extension attributes as a JSON string on that wire. After decoding, the ordinary server validator applies. The application protocol is included once in the provider instructions; the textual request does not repeat it or the operation schema.

The installed Codex app-server supplies paginated `model/list` capabilities. Each decision starts a thread with the persona's exact choice and provider fallback disabled. Application actions handle host commands, while native provider command tools are disabled. This keeps observed actions in the application loop and does not restrict which host commands it can execute.

For a model advertising image input, selected immutable PNG, JPEG or WebP artifacts become `localImage` inputs. Calls preserve their digest, purpose, path and actual wire inclusion. Unsupported or unadvertised image capability is recorded explicitly in context; metadata inspection alone is not visual assessment. The interface follows the [official app-server documentation](https://learn.chatgpt.com/docs/app-server).

The adapter preserves thread configuration, actual model identity returned by the provider, usage notifications, errors and raw events. A failed or interrupted request does not imply zero usage. Capacity errors do not silently switch models. An operator-authorized fallback is a separate model-choice operation with API provenance; subsequent persona choices carry their model-call provenance.

Additional providers use configured executable bridges. `--models` returns advertised model metadata. A normal invocation reads `ModelRequest` on stdin and returns `ModelResponse` on stdout. Standard error and returned bytes are retained. A bridge can use third-party provider SDKs and must implement any modalities it advertises. The persona's continuing identity and learning belong to the application.

Cross-provider live validation is explicitly deferred for the current campaign at the user's request to limit spending. Deterministic bridge tests establish interface mechanics only. Model usage reports cover what the application observes, not every request made by arbitrary host programs.
