from django.urls import path
from main.apps.simulation_data_mgt.actors.handoverSimJobManager import handoverSimJobManager

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
]
