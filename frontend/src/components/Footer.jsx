import { Link } from 'react-router-dom'

export default function Footer() {
    return (
        <footer className="
            bg-(--primary-color) px-5 py-3
            gap-y-5 flex flex-col
        ">
            <div className='
                flex justify-between
            '>
                <div className="
                    flex flex-col gap-y-5
                ">
                    <div>
                        <p>Analyzing Wikipedia Articles for better <br /> insights and discovery</p>
                    </div>
                    <div className="flex gap-x-2 items-center">
                        <div>
                            <img src="\facebook.svg" alt="Facebook Logo" className="w-11"
                            />
                        </div>
                        <div>
                            <img src="\linkedin.svg" alt="LinkedIn Logo" className="w-10"/>
                        </div>
                        <div>
                            <img src="\github.svg" alt="GitHub Logo" className="w-10"/>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <h1 className='
                            font-bold text-lg
                        '>Quick Links</h1>
                    </div>
                    <div>
                        <ul className='
                            ml-2 font-bold text-sm
                        '>
                            <li><Link>Home</Link></li>
                            <li><Link>Problem</Link></li>
                            <li><Link>Solution</Link></li>
                            <li><Link>FAQ's</Link></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div>
                        <h1 className='
                            font-bold text-lg
                        '>Contact Us</h1>
                    </div>
                    <div>
                        <div className='flex items-center gap-x-2'>
                            <img src="\email.svg" alt="Email Icon" className='w-5'/>
                            <p><Link>muelvinlopez25@gmail.com</Link></p>
                        </div>
                        <div className='flex items-center gap-x-2'>
                            <img src="\linkedin-icon.svg" alt="LinkedIn Icon" className='w-5'/>
                            <p><Link>Muelvin Lopez</Link></p>
                        </div>
                        <div className='flex items-center gap-x-2'>
                            <img src="\instagram-icon.svg" alt="Instagram Icon" className='w-5'/>
                            <p><Link>Muelvzz</Link></p>
                        </div>
                    </div>
                </div>
            </div>

            <div className='
                flex justify-between
            '>
                <div>
                    <p>© 2026 WikiWatch. All rights reserved.</p>
                </div>
                <div>
                    <p>Discover data that is hidden by a normal eye</p>
                </div>
            </div>
        </footer>
    )
}