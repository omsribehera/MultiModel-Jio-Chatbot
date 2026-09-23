import re

answer = '<|tool_call|>call:get_weather[city:"Goa"}<tool_call|>'
tool_call_match = re.search(r'<\|tool_call\|>\s*call:(get_weather|get_current_location)(.*?)(<\|/?tool_call\|>|<tool_call|>|$)', answer, re.IGNORECASE)
if tool_call_match:
    tool_name = tool_call_match.group(1)
    args_str = tool_call_match.group(2).strip()
    print("tool_name:", tool_name)
    print("args_str:", args_str)
    
    city_match = re.search(r'city\s*[:=]\s*"([^"]+)"', args_str.replace("'", '"'))
    if city_match:
        print("city:", city_match.group(1))
    else:
        print("city not found")
