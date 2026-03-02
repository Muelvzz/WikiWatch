import { useEffect, useState } from "react";

export default function NavBar() {

  const [width, setWidth] = useState(window.innerWidth)

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth)

    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  return (
    <nav className="bg-white text-black px-4 py-2">
      <div className="flex justify-between items-center">
        <div className="flex items-center gap-x-2 flex-1">
          <div>
            <img 
              src="public\logo.png" alt="Logo" 
              className="w-10"
            />
          </div>
          <div className="font-black lg:text-2xl text-xl flex">
            Wiki
            <div className="text-[#004643]">Watch</div>
          </div>
        </div>

        {
          width >= 1024 && (
          <div className="bg-[#a3a7a7] flex-1 flex rounded-md gap-x-1 p-1">
            <img src="public\search.png" alt="Search Icon" className="w-5"/>
            <input 
              type="text" 
              className="w-full font-light text-sm"
              placeholder="Wikipedia Link"
            />
          </div>
          )
        }

      </div>
    </nav>
  )
}