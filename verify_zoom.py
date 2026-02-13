from playwright.sync_api import sync_playwright
import time

def verify(page):
    print("Navigating to simulation...")
    page.goto("http://localhost:8080/index.html")

    print("Waiting for simulation to initialize...")
    page.wait_for_selector("#simulationCanvas")

    # Wait for particles
    time.sleep(3)

    print("Taking Main View screenshot...")
    page.screenshot(path="sim_main_view.png")

    # Simulate Click on a Node (e.g., Center of screen approx)
    # We need to find where a 'temple' or 'tower' is.
    # The FED is at lat 38, lon -77.
    # Rotation starts at 0.
    # We might need to rotate it or just click blindly in the center where we know nodes exist.
    # Let's try clicking the center of the canvas, there should be something or we drag to rotate.

    print("Attempting to click a node...")
    # Click slightly offset from center to hit a node
    page.mouse.click(page.viewport_size['width'] / 2, page.viewport_size['height'] / 2)

    time.sleep(1)
    print("Taking potential Zoom View screenshot...")
    page.screenshot(path="sim_zoom_view.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            verify(page)
        finally:
            browser.close()
