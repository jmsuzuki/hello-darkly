from suzuki_utils.dynamic_nested_import import dynamic_nested_import
from hello_darkly.src.features.i_feature import IFeature

FEATURES = dynamic_nested_import(
    file_from_package=__file__,
    file_name_from_package=__name__,
    type_to_import=IFeature,
    # exclude_modules=["factory"]
)


