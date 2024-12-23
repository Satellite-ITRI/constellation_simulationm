from django.urls import path
from main.apps.simulation_data_mgt.actors.handoverSimJobManager import handoverSimJobManager
from main.apps.simulation_data_mgt.actors.CoverageAnalysisSimJobManager import CoverageAnalysisSimJobManager
from main.apps.simulation_data_mgt.actors.connectionTimeSimJobManager import connectionTimeSimJobManager
from main.apps.simulation_data_mgt.actors.phaseParameterSelectionJobManager import phaseParameterSelectionJobManager


urlpatterns = [
    path('simulation_data_mgt/handoverSimJobManager/run_handover_sim_job',
         handoverSimJobManager.run_handover_sim_job, name="run_handover_sim_job"),
    path('simulation_data_mgt/handoverSimJobManager/delete_handover_sim_result',
         handoverSimJobManager.delete_handover_sim_result, name="delete_handover_sim_result"),
    path('simulation_data_mgt/handoverSimJobManager/download_handover_sim_result',
         handoverSimJobManager.download_handover_sim_result, name="download_handover_sim_result"),
    path('simulation_data_mgt/handoverSimJobManager/download_routing_sim_result_tmp',
         handoverSimJobManager.download_routing_sim_result_tmp, name="download_routing_sim_result_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_isl_sim_result_tmp',
         handoverSimJobManager.download_isl_sim_result_tmp, name="download_isl_sim_result_tmp"),
     path('simulation_data_mgt/CoverageAnalysisSimJobManager/test_post',
         CoverageAnalysisSimJobManager.test_post, name="test_post"),
     path('simulation_data_mgt/CoverageAnalysisSimJobManager/run_coverage_analysis_sim_job',
         CoverageAnalysisSimJobManager.run_coverage_analysis_sim_job, name="run_coverage_analysis_sim_job"),
     path('simulation_data_mgt/CoverageAnalysisSimJobManager/delete_coverage_analysis_sim_result',
         CoverageAnalysisSimJobManager.delete_coverage_analysis_sim_result, name="delete_coverage_analysis_sim_result"),

    path('simulation_data_mgt/connectionTimeSimJobManager/run_connection_time_sim_job',
         connectionTimeSimJobManager.run_connection_time_sim_job, name="run_connection_time_sim_job"),
    path('simulation_data_mgt/connectionTimeSimJobManager/delete_connection_time_sim_result',
         connectionTimeSimJobManager.delete_connection_time_sim_result, name="delete_connection_time_sim_result"),
    path('simulation_data_mgt/connectionTimeSimJobManager/download_connection_time_sim_result',
         connectionTimeSimJobManager.download_connection_time_sim_result, name="download_connection_time_sim_result"),

    path('simulation_data_mgt/phaseParameterSelectionJobManager/run_phase_parameter_selection_job',
         phaseParameterSelectionJobManager.run_phase_parameter_selection_job, 
         name="run_phase_parameter_selection_job"),

    path('simulation_data_mgt/phaseParameterSelectionJobManager/delete_phase_parameter_selection_result',
         phaseParameterSelectionJobManager.delete_phase_parameter_selection_result, 
         name="delete_phase_parameter_selection_result"),

    path('simulation_data_mgt/phaseParameterSelectionJobManager/download_phase_parameter_selection_result',
         phaseParameterSelectionJobManager.download_phase_parameter_selection_result, 
         name="download_phase_parameter_selection_result"),

    path('simulation_data_mgt/handoverSimJobManager/download_coverage_tmp',
         handoverSimJobManager.download_coverage_tmp, name="download_coverage_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_connected_duration_tmp',
         handoverSimJobManager.download_connected_duration_tmp, name="download_connected_duration_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_phase_tmp',
         handoverSimJobManager.download_phase_tmp, name="download_phase_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_constellation_strategy_tmp',
         handoverSimJobManager.download_constellation_strategy_tmp, name="download_constellation_strategy_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_isl_hopping_tmp',
         handoverSimJobManager.download_isl_hopping_tmp, name="download_isl_hopping_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_modify_regen_routing_tmp',
         handoverSimJobManager.download_modify_regen_routing_tmp, name="download_modify_regen_routing_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_one_to_multi_tmp',
         handoverSimJobManager.download_one_to_multi_tmp, name="download_one_to_multi_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_multi_to_multi_tmp',
         handoverSimJobManager.download_multi_to_multi_tmp, name="download_multi_to_multi_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_save_er_routing_tmp',
         handoverSimJobManager.download_save_er_routing_tmp, name="download_save_er_routing_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_end_to_end_routing_tmp',
         handoverSimJobManager.download_end_to_end_routing_tmp, name="download_end_to_end_routing_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_save_er_routing_tmp',
         handoverSimJobManager.download_save_er_routing_tmp, name="download_save_er_routing_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_single_beam_tmp',
         handoverSimJobManager.download_single_beam_tmp, name="download_single_beam_tmp"),
    path('simulation_data_mgt/handoverSimJobManager/download_gso_tmp',
         handoverSimJobManager.download_gso_tmp, name="download_gso_tmp"),
]
