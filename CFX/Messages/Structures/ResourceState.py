from enum import Enum

class ResourceState(Enum):
    """Endpoint state model.  Based on SEMI E10 and E58."""
    
    # Productive Time.  A period of time when the resource is performing its intended function.
    PRD = "1000"
    # Productive Time.  Regular Work.
    PRD_RegularWork = "1100"
    # Productive Time.  Work for Third Parties.
    PRD_WorkForThirdParties = "1200"
    # Productive Time.  Rework.
    PRD_Rework = "1300"
    # Productive Time.  Engineering.
    PRD_Engineering = "1400"
    # Standby.  A period of time, other than non-scheduled time, when the resource is in a condition to perform
    # its intended function, but it is not operating.
    SBY = "2000"
    # Standby.  No Operator.
    SBY_NoOperator = "2100"
    # Standby.  No Product 
    SBY_NoProduct = "2200"
    # Standby.  No Product (Resource is Blocked)
    SBY_NoProductBlocked = "2201"
    # Standby.  No Product (Resource is Starved)
    SBY_NoProductStarved = "2202"
    # Standby.  No Support Tool (A required Tool is missing.  For example, a stencil on a stencil printer.).
    SBY_NoSupportTool = "2300"
    # Standby.  Associated Cluster Module Down.
    SBY_AssociatedClusterModuleDown = "2400"
    # Standby.  No Host.  (Communication with a critical upper level controller or system has been lost, and 
    # resource cannot operate).
    SBY_NoHost = "2500"
    # Engineering.  A period of time when the resource is in a condition to perform its intended function (no equipment or
    # process problems exist), but it is operating to conduct engineering experiments.
    ENG = "3000"
    # Engineering.  Process experiments.
    ENG_ProcessExperiments = "3100"
    # Engineering.  Equipment experiments.
    ENG_EquipmentExperiments = "3200"
    # Scheduled Downtime.  A period of time when the resource is not available to perform its intended function due to 
    # planned downtime events.
    SDT = "4000"
    # Scheduled Downtime.  User Maintenance Delay.  Waiting for required maintenance personnel.
    SDT_UserMaintenanceDelay = "4100"
    # Scheduled Downtime.  Supply Maintenance Delay.  Waiting for parts required to perform maintenance.
    SDT_SuppliedMaintenanceDelay = "4200"
    # Scheduled Downtime.  Actively working on Preventive Maintenance procedures.
    SDT_PreventiveMaintenance = "4300"
    # Scheduled Downtime.  Scheduled changed of supply materials.
    SDT_ChangeOfConsumables = "4400"
    # Scheduled Downtime.  Scheduled setup time.
    SDT_Setup = "4500"
    # Scheduled Downtime.  Scheduled production testing.
    SDT_ProductionTest = "4600"
    # Scheduled Downtime.  Facilities related.
    SDT_FacilitiesRelated = "4700"
    # Unscheduled Downtime.  A period of time when the resource is not available to perform its intended
    # function due to unplanned downtime events.
    USD = "5000"
    # Unscheduled Downtime.  User Maintenance Delay.  Waiting for required maintenance personnel.
    USD_UserMaintentanceDelay = "5100"
    # Unscheduled Downtime.  User Supply Delay.  Waiting for parts required to perform maintenance.
    USD_SuppliedMaintenanceDelay = "5200"
    # Unscheduled Downtime.  Repair underway.
    USD_Repair = "5300"
    # Unscheduled Downtime.  A condition necessary for proper production is not in order.
    USD_OutOfSpecInputMaterial = "5400"
    # Unscheduled Downtime.  Supply material is empty, and needs to be changed.
    USD_ChangeOfConsumables = "5500"
    # Unscheduled Downtime.  Facilities related.
    USD_FacilitiesRelated = "5600"
    # Non-Scheduled Time.  A period of time when the resource is not scheduled to be utilized in production, such as unworked
    # shifts, weekends, and holidays (including startup and shutdown).
    NST = "6000"
    # Non-Scheduled Time.  Unworked shifts.
    NST_UnworkedShifts = "6100"
    # Non-Scheduled Time.  Equipment installation.
    NST_EquipmentInstallation = "6200"
    # Non-Scheduled Time.  Equipment modifications.
    NST_EquipmentModifications = "6300"
    # Non-Scheduled Time.  Offline training.
    NST_OfflineTraining = "6400"
    # Non-Scheduled Time.  Shutdown and Startup.
    NST_ShutdownAndStartup = "6500"