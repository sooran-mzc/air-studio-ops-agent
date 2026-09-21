# Use uv's ARM64 Python base image
FROM --platform=linux/arm64 ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

# Copy uv files
COPY pyproject.toml ./

# Install dependencies (including strands-agents)
RUN uv sync --no-cache

# Copy agent file
COPY agent.py ./

# Run as a non-root user
RUN useradd --create-home --uid 10001 app && chown -R app:app /app
USER app

# Expose port
EXPOSE 8080

# Run application (uv run would re-sync at runtime, so call the venv directly)
CMD ["/app/.venv/bin/uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8080"]
