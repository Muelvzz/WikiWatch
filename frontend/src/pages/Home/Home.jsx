const HeroSection = () => {
  return (
    <>
      <main className="flex  justify-center items-center h-full px-4">
        <article className="lg:w-3/4 flex flex-col lg:justify-center">

          <section
            className="text-4xl font-bold text-center"
          >
            Identify whether an Article is edited
          </section>

          <section className="text-center mt-10 mb-10">
            <b>Wikipedia isn't a finished book - it's a constant argument</b>. While we all know that anyone can edit a page - making it a risky source for academic or professional research - not every article is <b>"fake"</b>. <b>Many are the result of years of rigorous, high-quality consensus</b>, while others are curretnly being torn apart by 'edit wars' and biased agendas.
          </section>

          <section className="flex flex-col justify-center gap-y-5">
            <div className="bg-white flex-1 flex rounded-md gap-x-1 px-1 py-2">
              <img src="public\search.png" alt="Search Icon" className="w-5"/>
              <input 
                type="text" 
                className="w-full font-light text-sm text-black"
                placeholder="Wikipedia Link"
              />
            </div>
            <div className="flex justify-center">
              <button 
                className="
                  bg-[#004643] px-8 py-2 font-bold rounded-lg
                  hover:bg-[#122b30] duration-200 cursor-pointer
                  "
              >Documentations</button>
            </div>
          </section>

        </article>
      </main>
    </>
  )
}

export default HeroSection;
