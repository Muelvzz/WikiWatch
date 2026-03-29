export default function Button({text}) {
    return (
        <button
            className="
                bg-(--tertiary-color) text-white
                px-5 py-1 rounded-md cursor-pointer"
        >
            { text }
        </button>
    )
}