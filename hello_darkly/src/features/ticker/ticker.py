import time
from threading import Lock

from hello_darkly.src.features.i_feature import IFeature


def show_evaluation_result(key: str, value: bool):
    print()
    print(f"*** The {key} feature flag evaluates to {value}")


class FlagValueChangeListener:
    def __init__(self):
        self.__lock = Lock()

        self.__true_flag = False
        self.__ticker_value = 0
        self.show_ticker()

    def flag_value_change_listener(self, flag_change):
        with self.__lock:
            if flag_change.new_value:
                self.__true_flag = flag_change.new_value
                self.show_ticker()

            show_evaluation_result(flag_change.key, flag_change.new_value)

    def show_ticker(self):
        print("hello!  true_flag = ", self.__true_flag)
        self.__ticker_value += 1
        print(self.__ticker_value)
        time.sleep(1)


class Ticker(IFeature):
    # Set feature_flag_key to the feature flag key you want to evaluate.
    feature_flag_key = "ticker-feature"

    def __init__(self, ldclient, context):
        flag_value = ldclient.get().variation(self.feature_flag_key, context, False)
        show_evaluation_result(self.feature_flag_key, flag_value)

        flag_value_change_listener = FlagValueChangeListener()
        listener = ldclient.get().flag_tracker.add_flag_value_change_listener(
            self.feature_flag_key,
            context,
            flag_value_change_listener.flag_value_change_listener
        )


