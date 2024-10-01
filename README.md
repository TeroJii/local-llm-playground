# local-llm-playground

Testing out LLMs

## Running Ollama via Docker

Get the official image if you don't have it:

```bash
docker pull ollama/ollama
```

Run the image with:

```bash
docker run -d -p 11434:11434 --name ollama ollama/ollama
```

Pull the necessary models via:

```bash
docker exec -it ollama ollama pull <insert-model-name>
```

### Finding models

The [ollama website](https://ollama.com/library) lists available models.
