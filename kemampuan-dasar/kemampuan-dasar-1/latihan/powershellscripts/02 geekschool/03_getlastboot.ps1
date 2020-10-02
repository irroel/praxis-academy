param(
    [string]$ComputerName
)

Get-WmiObject -Class Win32_OperatingSystem |
Select-Object -Property CSName,@{n=”Last Booted”;

    e={[Management.ManagementDateTimeConverter]::ToDateTime($_.LastBootUpTime)}}