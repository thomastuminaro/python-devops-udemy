server_name = "webserver-03"
cpu_cores = 4
memory_gb = 8.0
disk_total_gb = 501
disk_used_gb = 352

disk_used_percentage = disk_used_gb / disk_total_gb
print(disk_used_percentage)

output_string = f"{server_name.upper()} {cpu_cores} {memory_gb} {round(disk_used_percentage, 1)}"
print(output_string)

print(f"Disk usage is {disk_used_percentage:.2%}")