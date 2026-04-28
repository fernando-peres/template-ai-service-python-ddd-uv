from enum import StrEnum


class ModelProvider(StrEnum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    OPENROUTER = "openrouter"


class AIModels(StrEnum):
    # *** Open AI ***
    # GPT-5 family
    OPEN_AI_GPT_5 = "gpt-5"
    OPEN_AI_GPT_5_MINI = "gpt-5-mini"
    OPEN_AI_GPT_5_NANO = "gpt-5-nano"

    # GPT-4.1 family
    OPEN_AI_GPT_4_1 = "gpt-4.1"
    OPEN_AI_GPT_4_1_MINI = "gpt-4.1-mini"
    OPEN_AI_GPT_4_1_NANO = "gpt-4.1-nano"

    # GPT-4o family
    OPEN_AI_GPT_4O = "gpt-4o"
    OPEN_AI_GPT_4O_MINI = "gpt-4o-mini"

    # Reasoning models
    OPEN_AI_O1 = "o1"
    OPEN_AI_O1_MINI = "o1-mini"
    OPEN_AI_O3 = "o3"
    OPEN_AI_O3_MINI = "o3-mini"

    # Embedding models
    OPEN_AI_TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"
    OPEN_AI_TEXT_EMBEDDING_3_LARGE = "text-embedding-3-large"

    # Moderation
    OPEN_AI_OMNI_MODERATION_LATEST = "omni-moderation-latest"

    # Audio / speech
    OPEN_AI_GPT_4O_TRANSCRIBE = "gpt-4o-transcribe"
    OPEN_AI_GPT_4O_MINI_TRANSCRIBE = "gpt-4o-mini-transcribe"
    OPEN_AI_GPT_4O_AUDIO = "gpt-4o-audio"

    # *** Open Router ***
    OPEN_ROUTER_GPT_4O_MINI = "openai/gpt-4o-mini"
    OPEN_ROUTER_GEMINI_3_PRO_IMAGE_PREVIEW = "google/gemini-3-pro-image-preview"
    OPEN_ROUTER_FLASH_GEMINI_2_5 = "google/gemini-2.5-flash"

    # *** Anthropic ***

    # *** Google ***
    GOOGLE_GEMINI_2_5_FLASH = "gemini-2.5-flash"
