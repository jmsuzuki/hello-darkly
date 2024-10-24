import os
import ldclient
from ldclient import Context
from ldclient.config import Config
from threading import Lock, Event

from hello_darkly.src.features.banner.banner import Banner


# Set sdk_key to your LaunchDarkly SDK key.
sdk_key = os.getenv("LAUNCHDARKLY_SDK_KEY")


if __name__ == "__main__":
    if not sdk_key:
        print("*** Please set the LAUNCHDARKLY_SDK_KEY env first")
        exit()

    ldclient.set_config(Config(sdk_key))

    if not ldclient.get().is_initialized():
        print("*** SDK failed to initialize. Please check your internet connection and SDK credential for any typo.")
        exit()

    print("*** SDK successfully initialized")

    # Set up the evaluation context. This context should appear on your
    # LaunchDarkly contexts dashboard soon after you run the demo.
    context = \
        Context.builder('example-user-key-2').kind('user').name('Drew').build()

    ### Included Features!
    banner = Banner(
        ldclient=ldclient,
        context=context
    )

    try:
        Event().wait()
    except KeyboardInterrupt:
        pass



