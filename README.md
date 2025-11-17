# 2025/11/17 09:22

# CFX Python SDK

[中文版本](#中文版本) | [English Version](#english-version)

---

## 中文版本

### 项目简介

本项目是一个针对使用CSharp语言开发的IPC CFX工具物联网通讯标准的SDK的Python实现。CFX（Connected Factory Exchange）是IPC制定的一种用于工业4.0环境中设备间通信的标准协议，旨在实现不同制造商设备之间的无缝数据交换。

### 项目解决的问题

1. **跨平台兼容性**：原CFX SDK主要基于C#开发，本项目提供了Python实现，使CFX协议能够在Python生态系统中使用
2. **简化集成**：为Python开发者提供了易于使用的CFX协议实现，降低了工业物联网应用的开发门槛
3. **协议完整性**：实现了CFX协议截至1.7.3版本的所有消息交互内容和结构体类的定义

### 项目特点

1. **基于AMQP 1.0协议**：使用AMQP 1.0作为底层通信协议，确保了消息传输的可靠性和标准化
2. **完整的CFX实现**：实现了CFX截至1.7.3版本的所有消息交互内容和结构体类的定义
3. **多种消息交互类型**：
   - 消息发布（Publish）：设备主动发送状态和事件信息
   - 消息接收（Receive）：接收来自其他设备或系统的消息
   - 请求/响应（Request/Response）：支持同步请求和响应模式
4. **模块化设计**：按照CFX消息类型进行模块化组织，便于使用和维护
5. **持续更新**：项目正在持续不断更新中，以适应CFX协议的最新发展

### 项目结构

```
CFXDemo/
├── CFX/                    # CFX协议实现核心代码
│   ├── CFXEnvelope.py      # CFX消息封装
│   ├── CFXMessage.py       # CFX消息基类
│   └── Messages/           # CFX消息实现
│       ├── CoreCommunication/  # 核心通信消息
│       ├── Maintenance/       # 维护相关消息
│       ├── Materials/         # 材料管理消息
│       ├── Production/        # 生产相关消息
│       ├── ResourcePerformance/  # 资源性能消息
│       └── Structures/        # 结构体定义
├── Amqp/                  # AMQP通信实现
└── SendDemo.py           # 示例代码
```

### 使用示例

```python
import asyncio

from Amqp.CFXContainer import CFXContainer
from Amqp.CFXEndpoint import CFXEndpoint
from CFX.CFXEnvelope import CFXEnvelope
from CFX.CFXMessage import CFXMessage
from CFX.Messages.CoreCommunication import *
from CFX.Messages.Production import *
from CFX.Messages.InformationSystem import *
from CFX.Messages.ResourcePerformance import *
from utils import logutils


class MyCFXEndpoint(CFXEndpoint):
    def __init__(self, local_url, cfx_handle):
        super(MyCFXEndpoint, self).__init__(local_url, cfx_handle)
        self.log_utils = logutils

    def on_message_receive_from_listener(self, msg) -> None:
        self.log_utils.critical_log("Message receive from listener")
        self.log_utils.critical_log(msg)

    def on_request_receive(self, request) -> [dict, None, CFXMessage]:
        self.log_utils.critical_log("Request receive")
        self.log_utils.critical_log(request)
        if request["MessageName"] == "CFX.AreYouThereRequest":
            return CFXEnvelope(message_body=AreYouThereResponse(self.cfx_handle, self.local_url,self.cfx_handle))
        return None


async def main():
    endpoint = MyCFXEndpoint("127.0.0.1:16666", "OriHandle")
    container = CFXContainer(endpoint, debug_info=True)
    container.set_heartbeat_frequency(60)
    container.add_publish_channel("127.0.0.1:18888", "listener")

    container.open_endpoint()

    container.publish_msg(
        CFXEnvelope(message_body=EndpointConnected(endpoint.cfx_handle, endpoint.local_url, endpoint.cfx_handle))
    )

    resp = await container.execute_request("127.0.0.1:18888", "local", CFXEnvelope(message_body=AreYouThereRequest(endpoint.cfx_handle)))
    print(resp)


if __name__ == '__main__':
    asyncio.run(main())
```

### 贡献指南

欢迎提交Issue和Pull Request来帮助改进本项目。在提交代码前，请确保：

1. 代码符合PEP 8规范
2. 添加适当的测试用例
3. 更新相关文档

---

## English Version

### Project Introduction

This project is a Python implementation of the IPC CFX (Connected Factory Exchange) IoT communication standard originally developed in C#. CFX is a standard protocol defined by IPC for communication between devices in Industry 4.0 environments, aiming to enable seamless data exchange between devices from different manufacturers.

### Problems Solved

1. **Cross-platform Compatibility**: The original CFX SDK is primarily based on C#, and this project provides a Python implementation, enabling the CFX protocol to be used in the Python ecosystem.
2. **Simplified Integration**: Provides an easy-to-use CFX protocol implementation for Python developers, lowering the barrier to developing industrial IoT applications.
3. **Protocol Completeness**: Implements all message interaction content and structure class definitions of the CFX protocol up to version 1.7.3.

### Project Features

1. **Based on AMQP 1.0 Protocol**: Uses AMQP 1.0 as the underlying communication protocol, ensuring reliable and standardized message transmission.
2. **Complete CFX Implementation**: Implements all message interaction content and structure class definitions of CFX up to version 1.7.3.
3. **Multiple Message Interaction Types**:
   - Message Publish: Devices actively send status and event information
   - Message Receive: Receive messages from other devices or systems
   - Request/Response: Supports synchronous request and response patterns
4. **Modular Design**: Organized according to CFX message types for ease of use and maintenance.
5. **Continuous Updates**: The project is continuously being updated to adapt to the latest developments in the CFX protocol.

### Project Structure

```
CFXDemo/
├── CFX/                    # Core CFX protocol implementation
│   ├── CFXEnvelope.py      # CFX message envelope
│   ├── CFXMessage.py       # CFX message base class
│   └── Messages/           # CFX message implementations
│       ├── CoreCommunication/  # Core communication messages
│       ├── Maintenance/       # Maintenance-related messages
│       ├── Materials/         # Material management messages
│       ├── Production/        # Production-related messages
│       ├── ResourcePerformance/  # Resource performance messages
│       └── Structures/        # Structure definitions
├── Amqp/                  # AMQP communication implementation
└── SendDemo.py           # Example code
```

### Usage Example

```python
import asyncio

from Amqp.CFXContainer import CFXContainer
from Amqp.CFXEndpoint import CFXEndpoint
from CFX.CFXEnvelope import CFXEnvelope
from CFX.CFXMessage import CFXMessage
from CFX.Messages.CoreCommunication import *
from CFX.Messages.Production import *
from CFX.Messages.InformationSystem import *
from CFX.Messages.ResourcePerformance import *
from utils import logutils


class MyCFXEndpoint(CFXEndpoint):
    def __init__(self, local_url, cfx_handle):
        super(MyCFXEndpoint, self).__init__(local_url, cfx_handle)
        self.log_utils = logutils

    def on_message_receive_from_listener(self, msg) -> None:
        self.log_utils.critical_log("Message receive from listener")
        self.log_utils.critical_log(msg)

    def on_request_receive(self, request) -> [dict, None, CFXMessage]:
        self.log_utils.critical_log("Request receive")
        self.log_utils.critical_log(request)
        if request["MessageName"] == "CFX.AreYouThereRequest":
            return CFXEnvelope(message_body=AreYouThereResponse(self.cfx_handle, self.local_url,self.cfx_handle))
        return None


async def main():
    endpoint = MyCFXEndpoint("127.0.0.1:16666", "OriHandle")
    container = CFXContainer(endpoint, debug_info=True)
    container.set_heartbeat_frequency(60)
    container.add_publish_channel("127.0.0.1:18888", "listener")

    container.open_endpoint()

    container.publish_msg(
        CFXEnvelope(message_body=EndpointConnected(endpoint.cfx_handle, endpoint.local_url, endpoint.cfx_handle))
    )

    resp = await container.execute_request("127.0.0.1:18888", "local", CFXEnvelope(message_body=AreYouThereRequest(endpoint.cfx_handle)))
    print(resp)


if __name__ == '__main__':
    asyncio.run(main())
```

### Contributing Guidelines

Issues and Pull Requests are welcome to help improve this project. Before submitting code, please ensure:

1. Code complies with PEP 8 standards
2. Add appropriate test cases
3. Update relevant documentation

