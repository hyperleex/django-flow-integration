import uuid
from typing import Dict, List

from accounts.services.base import BaseFlowService


class AccountService(BaseFlowService):
    def list(self) -> List[Dict]:
        return self._send_request("get", "accounts")

    def get(self, address: str) -> Dict:
        return self._send_request("get", f"accounts/{address}")

    def create(self) -> Dict:
        return self._send_request(
            "post", "accounts", headers={"Idempotency-Key": str(uuid.uuid4())}
        )
