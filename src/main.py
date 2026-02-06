import sys
from compositor.compositor import UnityXCompositor

def main():
    try:
        unityx = UnityXCompositor()
        unityx.run()
    except KeyboardInterrupt:
        print("\nUnityX shut down by user.")
        sys.exit(0)
    except Exception as e: # pylint: disable=broad-exception-caught
        print(f"UnityX failed to start: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
