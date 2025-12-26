

''' Note: The dir() function can be used on all modules, also the ones you create yourself. '''

import platform

x = dir(platform)
print(x)

''' Output: ['AndroidVer', 'IOSVersionInfo', '_Processor', '_WIN32_CLIENT_RELEASES', '_WIN32_SERVER_RELEASES', 
'__builtins__', '__cached__', '__copyright__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__spec__', '__version__', '_comparable_version', '_default_architecture', '_follow_symlinks', 
'_get_machine_win32', '_java_getprop', '_mac_ver_xml', '_node', '_norm_version', '_os_release_cache', 
'_os_release_candidates', '_parse_os_release', '_platform', '_platform_cache', '_sys_version', 
'_sys_version_cache', '_syscmd_file', '_syscmd_ver', '_uname_cache', '_unknown_as_blank', '_ver_stages', 
'_win32_ver', '_wmi', '_wmi_query', 'android_ver', 'architecture', 'collections', 'freedesktop_os_release',
 'functools', 'ios_ver', 'itertools', 'java_ver', 'libc_ver', 'mac_ver', 'machine', 'node', 'os', 'platform', 
 'processor', 'python_branch', 'python_build', 'python_compiler', 'python_implementation', 'python_revision',
   'python_version', 'python_version_tuple', 're', 'release', 'sys', 'system', 'system_alias', 'uname', 
   'uname_result', 'version', 'win32_edition', 'win32_is_iot', 'win32_ver']
PS D:\Python_Tutorial> '''
