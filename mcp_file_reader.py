import asyncio, os, shutil
from agents import Agent, Runner, gen_trace_id, trace
from agent.mcp import MCPServer, MCPServerStdio

async def run(mcp_server: MCPServer):
    # create the agent with the server
    agent=Agent("file reader", instruction="you help with reading files in a directory by making use of the mcp server provided to you", mcp_server=[mcp_server])
    
    # List all the files it can read
    msg="list all the files in the directory"
    print("running "+msg)
    files=Runner.run(agent, msg)
    print(files.final_output)
    
    # ask about my favourite book
    msg="what is my favourite book?"
    print("running "+msg)
    fav_book=Runner.run(agent,msg)
    print(fav_book.final_output)
    
    
    # Ask a question that reads then reasons
    msg="Look at my favourite sonbgs and suggest a new song based on it"
    print("running "+msg)
    song_recommendation=Runner.run(agent, msg)
    print(song_recommendation.final_output)
    
    
async def main():
    current_dir=os.path.dirname(os.path.abspath(__file__))
    sample_dir=os.path.join(current_dir+"sample_files")
    
    with MCPServerStdio as (
    name="file system server, via npx",
    params={
    command: "npx",
    args=[-y,"@modelcontextprotocol/server-filesystem", sample_dir]
    }
    ) as server:
        trace_id=gen_trace_id()
        
        with trace(workflow_name="file_reader_workflow", trace_id=trace_id):
            run(server)
            
            

if __name__=="__main__":
    if not shutil.which("npx"):
        raise RuntimeError("npx is not installed. Please install it with `npm install -g npx`.")

    asyncio.run(main())
    
    