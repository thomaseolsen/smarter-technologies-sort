import sys
import argparse
import logging

from utils import sort

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


def parse_args(argv=None):
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Runnable Sorter")
    parser.add_argument(
        "--width", help="Width of the package in centimeters", type=int, required=True
    )
    parser.add_argument(
        "--height", help="Height of the package in centimeters", type=int, required=True
    )
    parser.add_argument(
        "--length", help="Length of the package in centimeters", type=int, required=True
    )
    parser.add_argument(
        "--mass", help="Mass of the package in kilograms", type=float, required=True
    )
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    logger.info(
        "Sorting package of dimensions (WxHxL): %dx%dx%d cm and mass: %.2f kg",
        args.width,
        args.height,
        args.length,
        args.mass,
    )

    # Example usage
    print(sort(args.width, args.height, args.length, args.mass))

    return 0


if __name__ == "__main__":
    sys.exit(main())
