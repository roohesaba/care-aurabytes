export default function FileList({ files }) {
  return (
    <ul>
      {files.map(file => (
        <li key={file.id}>{file.name}</li>
      ))}
    </ul>
  );
}