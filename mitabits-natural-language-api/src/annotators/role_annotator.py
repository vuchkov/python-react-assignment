import re
import yaml
from pathlib import Path
from typing import List, Dict, Any

class RoleAnnotator:
    def __init__(self):
        self.roles = self._load_roles()
        self.pattern = self._build_pattern()

    def _load_roles(self) -> List[str]:
        roles_path = Path(__file__).parent.parent / 'resources' / 'roles.yml'
        with open(roles_path, 'r') as f:
            data = yaml.safe_load(f)
        return data.get('roles', [])

    def _build_pattern(self) -> re.Pattern:
        # Create regex pattern matching any role (with word boundaries)
        roles_pattern = '|'.join(map(re.escape, self.roles))
        return re.compile(rf'\b({roles_pattern})\b', re.IGNORECASE)

    def annotate(self, text: str) -> List[Dict[str, Any]]:
        annotations = []
        for match in self.pattern.finditer(text):
            annotations.append({
                'type': 'ROLE',
                'content': match.group(),
                'start': match.start(),
                'end': match.end(),
                'meta': {'source': 'role_annotator'}
            })
        return annotations
