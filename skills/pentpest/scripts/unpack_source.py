"""Extract bundled, pinned upstream source without executing it."""
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parents[1]
target=root/'assets/upstream'
with zipfile.ZipFile(root/'assets/upstream-source.zip') as z:
    for entry in z.infolist():
        path=Path(entry.filename)
        if path.is_absolute() or '..' in path.parts or (entry.external_attr >> 16) & 0o170000 == 0o120000:
            raise ValueError('Unsafe archive member')
    z.extractall(target)
print(target)
