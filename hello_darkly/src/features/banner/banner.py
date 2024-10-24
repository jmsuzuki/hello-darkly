from threading import Lock

from hello_darkly.src.features.i_feature import IFeature


class Banner(IFeature):
    # Set feature_flag_key to the feature flag key you want to evaluate.
    feature_flag_key = "sample-feature"

    def __init__(self, ldclient, context):
        self.__show_banner = True
        self.__lock = Lock()

        flag_value = ldclient.get().variation(self.feature_flag_key, context, False)
        self.show_evaluation_result(self.feature_flag_key, flag_value)

        listener = ldclient.get().flag_tracker.add_flag_value_change_listener(
            self.feature_flag_key,
            context,
            self.flag_value_change_listener
        )

    def flag_value_change_listener(self, flag_change):
        with self.__lock:
            if self.__show_banner and flag_change.new_value:
                self.show_banner()
                self.__show_banner = False

            self.show_evaluation_result(flag_change.key, flag_change.new_value)

    def show_evaluation_result(self, key: str, value: bool):
        print()
        print(f"*** The {key} feature flag evaluates to {value}")

    def show_banner(self):
        print()
        print("        ██       ")
        print("          ██     ")
        print("      ████████   ")
        print("         ███████ ")
        print("██ LAUNCHDARKLY █")
        print("         ███████ ")
        print("      ████████   ")
        print("          ██     ")
        print("        ██       ")
        print()


