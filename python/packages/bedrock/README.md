# Get Started with Spark Core Bedrock

Install the provider package:

```bash
pip install spark-core-bedrock --pre
```

## Bedrock Integration

The Bedrock integration enables Spark Core applications to call Amazon Bedrock models with familiar chat abstractions, including tool/function calling when you attach tools through `ChatOptions`.

### Basic Usage Example

See the [Bedrock sample](../../samples/02-agents/providers/amazon/bedrock_chat_client.py) for a runnable end-to-end script that:

- Loads credentials from the `BEDROCK_*` environment variables
- Instantiates `BedrockChatClient`
- Sends a simple conversation turn and prints the response
