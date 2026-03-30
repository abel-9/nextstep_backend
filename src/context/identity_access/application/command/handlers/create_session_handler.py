# datetime
from datetime import datetime, timezone

# Commands
from src.context.identity_access.application.command.commands import (
    CreateSessionCommand,
)

# Application Ports
from src.context.shared_kernel.application.ports import ITokenService

# DTOS
from src.context.identity_access.application.command.dtos import (
    TokenResponseDto,
    AccessSession,
)


class CreateSessionHandler:
    def __init__(self, token_service: ITokenService):
        self.__token_service = token_service

    async def __call__(self, cmd: CreateSessionCommand) -> TokenResponseDto:
        now = datetime.now(timezone.utc)
        access_session = AccessSession(
            sub=cmd.user_id,
            exp=now + AccessSession.get_exp_timedelta(),
            iat=now,
        )

        return TokenResponseDto(
            access_token=await self.__token_service.sign(
                payload=access_session.__dict__
            ),
            token_type="bearer",
        )
