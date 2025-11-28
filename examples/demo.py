#!/usr/bin/env python3
"""
Demo script for IR Downloader
Shows how to use the downloader programmatically
"""

import sys
import os

# Add parent directory to path to import IRDownloader
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from ir_downloader import IRDownloader
except ImportError:
    print("Error: Make sure ir_downloader.py is in the parent directory")
    sys.exit(1)

def demo():
    """Demonstrate IR Downloader capabilities"""
    print("🚀 IR Downloader - Demo Mode")
    print("=" * 50)
    
    # Create downloader instance
    downloader = IRDownloader()
    
    # Example URLs for testing (replace with actual URLs)
    test_urls = [
        "https://httpbin.org/bytes/1024",  # 1KB test file
        # Add more test URLs here
    ]
    
    print(f"\n📊 Platform: {downloader.platform_info['system']}")
    print(f"📁 Download Directory: {downloader.download_dir}")
    
    print(f"\n🎯 Available test URLs:")
    for i, url in enumerate(test_urls, 1):
        print(f"  {i}. {url}")
    
    print(f"\n💡 Usage Tips:")
    print("  - Enter full URL starting with http:// or https://")
    print("  - Type 'stats' to see download statistics")
    print("  - Type 'exit' to quit")
    print("  - Press Ctrl+C to interrupt current download")
    
    print(f"\n✨ Demo completed successfully!")

if __name__ == "__main__":
    demo()
