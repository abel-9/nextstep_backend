from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True,
        env_ignore_empty=True,
    )

    # APP
    TITLE: str
    DESCRIPTION: str
    VERSION: str
    PORT: int

    # DB
    DB_URL: str
    WRITE_DB_NAME: str
    READ_DB_NAME: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # Message Broker
    RABBITMQ_HOST: str
    RABBITMQ_EXCHANGE_NAME: str | None = None
    QUEUE_NAME: str

    # OAUTH
    OAUTH_TOKEN_URL: str

    # Gemini API
    GEMINI_API_KEY: str


settings = Settings()
