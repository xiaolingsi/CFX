import enum


class ResourceState(enum.Enum):
    PRD = 1000 
    PRD_RegularWork = 1100 
    PRD_WorkForThirdParties = 1200 
    PRD_Rework = 1300 
    PRD_Engineering = 1400 
    SBY = 2000 
    SBY_NoOperator = 2100 
    SBY_NoProduct = 2200 
    SBY_NoProductBlocked = 2201 
    SBY_NoProductStarved = 2202 
    SBY_NoSupportTool = 2300 
    SBY_AssociatedClusterModuleDown = 2400 
    SBY_NoHost = 2500 
    ENG = 3000 
    ENG_ProcessExperiments = 3100 
    ENG_EquipmentExperiments = 3200 
    SDT = 4000 
    SDT_UserMaintenanceDelay = 4100 
    SDT_SuppliedMaintenanceDelay = 4200 
    SDT_PreventiveMaintenance = 4300 
    SDT_ChangeOfConsumables = 4400 
    SDT_Setup = 4500 
    SDT_ProductionTest = 4600 
    SDT_FacilitiesRelated = 4700 
    USD = 5000 
    USD_UserMaintentanceDelay = 5100 
    USD_SuppliedMaintenanceDelay = 5200 
    USD_Repair = 5300 
    USD_OutOfSpecInputMaterial = 5400 
    USD_ChangeOfConsumables = 5500 
    USD_FacilitiesRelated = 5600 
    NST = 6000 
    NST_UnworkedShifts = 6100 
    NST_EquipmentInstallation = 6200 
    NST_EquipmentModifications = 6300 
    NST_OfflineTraining = 6400 
    NST_ShutdownAndStartup = 650 
