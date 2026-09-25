# Stable Fast 3D - Python 3.13 Patches

This repository automatically patches and builds Stable Fast 3D for Python 3.13 compatibility.

## Quick Start

### Use the Pre-Built Wheels

1. Go to [Releases](../../releases)
2. Download the wheels for Python 3.13
3. Install in Colab:

```python
!pip install https://github.com/YOUR_USERNAME/stable-fast-3d-python313-patches/releases/download/v1.0.0-py313/texture_baker-0.1.0-cp313-cp313-linux_x86_64.whl
!pip install https://github.com/YOUR_USERNAME/stable-fast-3d-python313-patches/releases/download/v1.0.0-py313/uv_unwrapper-0.1.0-cp313-cp313-linux_x86_64.whl
```

### Build Your Own Wheels

1. Fork this repository
2. Go to Actions → Auto-Patch and Build
3. Click "Run workflow"
4. Wait ~15 minutes
5. Download wheels from Releases

## How It Works

This workflow:
1. Clones the official Stable Fast 3D repository
2. Attempts to build it on Python 3.13
3. Captures compilation errors
4. Automatically patches C++ code for Python 3.13 compatibility
5. Rebuilds and publishes working wheels

## Supported Python Versions

- ✅ Python 3.13 (auto-patched)
- ✅ Python 3.12 (native support)
- ✅ Python 3.11 (native support)
- ✅ Python 3.10 (native support)

## License

Same as Stable Fast 3D (Stability AI Community License)
