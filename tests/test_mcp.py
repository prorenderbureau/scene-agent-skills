import asyncio
import os
import sys
import pytest
pytest.importorskip('mcp')

def test_real_stdio_handshake_tools_and_path_guard(tmp_path):
    from mcp import ClientSession,StdioServerParameters
    from mcp.client.stdio import stdio_client
    async def run():
        env=dict(os.environ,SCENE_AGENT_WORKSPACE=str(tmp_path))
        params=StdioServerParameters(command=sys.executable,args=['-m','scene_agent.server'],env=env)
        async with stdio_client(params) as (read,write):
            async with ClientSession(read,write) as session:
                await session.initialize()
                tools=await session.list_tools()
                assert len(tools.tools)==6
                result=await session.call_tool('list_styles',{})
                assert not result.isError and 'blue-hour' in str(result)
                good=await session.call_tool('prepare_corona_script',{'relative_output':'preview.ms','quality':'preview'})
                assert not good.isError and (tmp_path/'preview.ms').exists()
                overwrite=await session.call_tool('prepare_corona_script',{'relative_output':'preview.ms'})
                assert overwrite.isError
                bad=await session.call_tool('check_plan',{'relative_path':'../outside.json'})
                assert bad.isError
    asyncio.run(run())
