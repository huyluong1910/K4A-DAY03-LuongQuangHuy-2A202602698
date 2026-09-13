"""
🔌 MODEL CONTEXT PROTOCOL (MCP) SERVER MODULE
Mô phỏng kiến trúc MCP Server (Client-Server Architecture) cung cấp công cụ chuẩn hóa.
"""

import json
import sys
from typing import Dict, Any, List
from tools import TOOLS_SCHEMA, dispatch_tool_call

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass


class MCPAcademicServer:
    """
    Giả lập MCP Server tuân thủ chuẩn giao thức Model Context Protocol
    """

    def __init__(self, server_name: str = "vinuni-academic-mcp-server"):
        self.server_name = server_name
        self.version = "2026.1.0"
        self.tools = TOOLS_SCHEMA  # Khởi tạo thuộc tính self.tools

    def list_tools(self) -> List[Dict[str, Any]]:
        """Trả về danh sách các Tools chuẩn giao thức MCP"""
        return self.tools

    def call_tool(self, tool_name: str, arguments: dict) -> dict:
        """
        Task 2.1: Tiếp nhận yêu cầu gọi Tool từ Agent (MCP Client),
        thực thi qua dispatch_tool_call và đóng gói chuẩn JSON-RPC 2.0.
        """
        try:
            # Thực thi tool và nhận kết quả từ tools.py
            raw_result = dispatch_tool_call(tool_name, arguments)

            return {
                "jsonrpc": "2.0",
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": raw_result
                        }
                    ],
                    "isError": False
                },
                "id": 1
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "error": {
                    "code": -32603,
                    "message": str(e)
                },
                "id": 1
            }


if __name__ == "__main__":
    print("==========================================================")
    print("🔌 KIỂM THỬ ĐỘC LẬP MCP SERVER (vinuni-academic-mcp-server)")
    print("==========================================================")

    server = MCPAcademicServer()
    tools = server.list_tools()
    print(f"✅ Khởi tạo thành công MCP Server: {server.server_name} (Version: {server.version})")
    print(f"📦 Số lượng Tools công bố: {len(tools)}")

    # Kiểm tra trạng thái TODO 1.2 (Tool Schema)
    sched_tool = next((t for t in tools if t.get("name") == "schedule_appointment"), None)
    if sched_tool and not sched_tool.get("parameters", {}).get("properties"):
        print("⏳ [TODO 1.2]: Tool 'schedule_appointment' chưa được định nghĩa properties trong 'src/tools.py'.")
    else:
        print("✅ [TODO 1.2]: Tool 'schedule_appointment' đã có schema đầy đủ.")

    # Kiểm tra trạng thái TODO 2.1 (call_tool)
    test_result = server.call_tool("academic_query", {"student_id": "SV2026001"})
    if not test_result:
        print("⏳ [TODO 2.1]: Hàm call_tool() đang trả về rỗng. Học viên hãy hoàn thiện TODO 2.1 trong 'src/mcp_server.py'!")
    else:
        print(f"✅ [TODO 2.1]: Test dispatch tool 'academic_query' thành công:")
        print(f"   Phản hồi JSON-RPC: {json.dumps(test_result, ensure_ascii=False)}")