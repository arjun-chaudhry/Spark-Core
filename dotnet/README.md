# Get Started with Spark Core for C# Developers

## Quickstart

### Basic Agent - .NET

```c#
using Azure.AI.OpenAI;
using Azure.Identity;
using Microsoft.Agents.AI;
using OpenAI.Responses;

var endpoint = Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!;
var deploymentName = Environment.GetEnvironmentVariable("AZURE_OPENAI_DEPLOYMENT_NAME")!;

var agent = new AzureOpenAIClient(new Uri(endpoint), new AzureCliCredential())
    .GetResponsesClient(deploymentName)
    .AsAIAgent(name: "HaikuBot", instructions: "You are an upbeat assistant that writes beautifully.");

Console.WriteLine(await agent.RunAsync("Write a haiku about Spark Core."));
```

## Examples & Samples

- [Getting Started with Agents](./samples/02-agents/Agents): basic agent creation and tool usage
- [Agent Provider Samples](./samples/02-agents/AgentProviders): samples showing different agent providers
- [Workflow Samples](./samples/03-workflows): advanced multi-agent patterns and workflow orchestration

## Spark Core Documentation

- [Documentation](https://learn.microsoft.com/spark-core/)
- [Spark Core Repository](https://github.com/microsoft/spark-core)
- [Design Documents](../docs/design)
- [Architectural Decision Records](../docs/decisions)
- [MSFT Learn Docs](https://learn.microsoft.com/spark-core/overview/spark-core-overview)

