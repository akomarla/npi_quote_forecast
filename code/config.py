# -*- coding: utf-8 -*-

# Standard execution

# Pegatron read and write paths
pegatron_read_file_path = "S:/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_files/anchored_data/Solidigm Pegatron NPI Quote File.xlsm"
pegatron_write_file_path = "//npcorpgobufileshares.file.core.windows.net/bi-share/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_forecast/anchored_results/NPI Pegatron Forecasts.xlsx"
pegatron_name = 'PEGATRON' 

# PTI read and write paths
pti_read_file_path = "S:/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_files/anchored_data/Solidigm PTI TW NPI Quote File.xlsm"
pti_write_file_path = "//npcorpgobufileshares.file.core.windows.net/bi-share/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_forecast/anchored_results/NPI PTI Forecasts.xlsx"
pti_name = 'PTI TAIWAN'

# Combined output write path
pti_pegatron_write_file_path = "//npcorpgobufileshares.file.core.windows.net/bi-share/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_forecast/anchored_results/NPI PTI & Pega Forecasts.xlsx"
pti_pegatron_name = 'PEGATRON and PTI TAIWAN'

# Same for all ODMs
ignore_sheets = ['Input', 'MainSheet']
excel_output = True
log_file_path = "S:/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_forecast/anchored_results/forecasting_log.log"
ww_range_allowed = [202241, 202253]
ww_col = 'Req WW (WW enterd)'
build_status_allowed = ['ACTIVE', 'WIP', 'DONE']
level = 'Product Code'
ft_method = {'BOM+MVA Cost': ['mean', 'weighted mean'], 'Subtotal = NRE+\nQty*(BOM+MVA)': ['mean']}
weight_col = 'Build Qty'


# Testing 

# Pegatron file paths for test data and true results computed by hand
pegatron_read_test_file_path = "S:/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_files/test_data/Solidigm Pegatron NPI Quote File.xlsm"
pegatron_read_true_result_file_path = "S:/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_forecast/test_results/NPI Pegatron Forecasts.xlsx"

# Pegatron file paths for test data and true results computed by hand
pti_read_test_file_path = "S:/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_files/test_data/Solidigm PTI TW NPI Quote File.xlsm"
pti_read_true_result_file_path = "S:/Global Supply Planning/gbl_ops_data_analytics.npi.application.quote_forecasting/odm_quote_forecast/test_results/NPI PTI TW Forecasts.xlsx"

# Same for both ODMs
test_col = 'Forecast for: BOM+MVA Cost (mean)'
test_ww_range_allowed = [202241, 202253]
test_build_status_allowed = ['ACTIVE', 'WIP', 'DONE']
